"""
Funciones de degradación de imágenes y generación de kernels personalizadas.
Reemplaza parcialmente el módulo degradations de basicsr.
"""
import math
import random
import torch
import numpy as np
from torch.nn import functional as F

def rgb_to_grayscale(img):
    if img.shape[0] != 3:
        raise ValueError('Input image must have 3 channels')
    weights = torch.tensor([0.2989, 0.5870, 0.1140], device=img.device)
    return torch.sum(img * weights.view(-1,1,1), dim=0, keepdim=True)

def random_add_gaussian_noise_pt(img, sigma_range=(0, 1.0), gray_prob=0, noise_gray_prob=0, clip=True, rounds=False):
    sigma = random.uniform(*sigma_range)
    if random.random() < gray_prob:
        img = rgb_to_grayscale(img)

    if random.random() < noise_gray_prob:
        noise = torch.randn(*img.shape[1:], device=img.device).unsqueeze(0).repeat(img.shape[0],1,1)
    else:
        noise = torch.randn_like(img) * sigma

    out = img + noise
    if clip and rounds:
        out = torch.clamp((out*255).round(), 0, 255)/255.
    elif clip:
        out = torch.clamp(out, 0, 1)
    elif rounds:
        out = (out*255).round()/255.
    return out

def random_add_poisson_noise_pt(img, scale_range=(0,1.0), gray_prob=0, clip=True, rounds=False):
    scale = random.uniform(*scale_range)
    if random.random() < gray_prob:
        img = rgb_to_grayscale(img)
    noise = torch.poisson(img*scale)/scale - img
    out = img + noise
    if clip and rounds:
        out = torch.clamp((out*255).round(), 0, 255)/255.
    elif clip:
        out = torch.clamp(out, 0, 1)
    elif rounds:
        out = (out*255).round()/255.
    return out

def circular_lowpass_kernel(cutoff, kernel_size, pad_to=0):
    if pad_to == 0: pad_to = kernel_size
    assert pad_to >= kernel_size

    def _sinc(x):
        return torch.tensor(1.) if x==0 else torch.sin(x*math.pi)/ (x*math.pi)

    half = (kernel_size-1)/2
    grid = torch.linspace(-half, half, kernel_size)
    x, y = torch.meshgrid(grid, grid)
    dist = torch.sqrt(x**2 + y**2)
    kernel = _sinc(dist*cutoff)
    kernel = kernel / kernel.sum()
    if pad_to > kernel_size:
        pad = (pad_to - kernel_size)//2
        kernel = F.pad(kernel, [pad]*4)
    return kernel

def random_mixed_kernels(kernel_list, kernel_prob, kernel_size=21, blur_sigma_min=0.1, blur_sigma_max=10.0, pad_to=0):
    ktype = np.random.choice(kernel_list, p=kernel_prob)
    if pad_to==0: pad_to=kernel_size

    if ktype=='iso':
        sigma = np.random.uniform(blur_sigma_min, blur_sigma_max)
        return _generate_isotropic_gaussian_kernel(kernel_size, sigma, pad_to)
    elif ktype=='aniso':
        sigma_x = np.random.uniform(blur_sigma_min, blur_sigma_max)
        sigma_y = np.random.uniform(blur_sigma_min, blur_sigma_max)
        rotation = np.random.uniform(-np.pi, np.pi)
        return _generate_anisotropic_gaussian_kernel(kernel_size, sigma_x, sigma_y, rotation, pad_to)
    else:
        return circular_lowpass_kernel(blur_sigma_min, kernel_size, pad_to)

def _generate_isotropic_gaussian_kernel(kernel_size, sigma, pad_to=0):
    if pad_to==0: pad_to=kernel_size
    half=(kernel_size-1)/2
    grid = torch.linspace(-half, half, kernel_size)
    x,y = torch.meshgrid(grid, grid)
    kernel = torch.exp(-(x**2+y**2)/(2*sigma**2))
    kernel = kernel/kernel.sum()
    if pad_to>kernel_size:
        pad=(pad_to-kernel_size)//2
        kernel=F.pad(kernel,[pad]*4)
    return kernel

def _generate_anisotropic_gaussian_kernel(kernel_size, sigma_x, sigma_y, rotation, pad_to=0):
    if pad_to==0: pad_to=kernel_size
    half=(kernel_size-1)/2
    grid=torch.linspace(-half, half, kernel_size)
    x,y=torch.meshgrid(grid, grid)
    cos_theta=torch.cos(torch.tensor(rotation))
    sin_theta=torch.sin(torch.tensor(rotation))
    x_rot=cos_theta*x - sin_theta*y
    y_rot=sin_theta*x + cos_theta*y
    kernel=torch.exp(-(x_rot**2/(2*sigma_x**2) + y_rot**2/(2*sigma_y**2)))
    kernel = kernel/kernel.sum()
    if pad_to>kernel_size:
        pad=(pad_to-kernel_size)//2
        kernel=F.pad(kernel,[pad]*4)
    return kernel
