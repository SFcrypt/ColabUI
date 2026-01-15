# Implementación personalizada de degradaciones para BasicSR
# Incluye ruido gaussiano, ruido Poisson y kernels de desenfoque

import cv2
import math
import random
import numpy as np
import torch
from torch.nn import functional as F

def random_add_gaussian_noise_pt(img, sigma_range=(0, 1.0), gray_prob=0, noise_gray_prob=0, clip=True, rounds=False):
    noise_sigma = random.uniform(*sigma_range)
    if random.random() < gray_prob:
        img = rgb_to_grayscale(img)
    noise = torch.randn_like(img) * noise_sigma
    out = img + noise
    if clip:
        out = torch.clamp(out, 0, 1)
    return out

def random_add_poisson_noise_pt(img, scale_range=(0, 1.0), gray_prob=0, clip=True, rounds=False):
    scale = random.uniform(*scale_range)
    if random.random() < gray_prob:
        img = rgb_to_grayscale(img)
    noise = torch.poisson(img * scale) / scale - img
    out = img + noise
    if clip:
        out = torch.clamp(out, 0, 1)
    return out

def rgb_to_grayscale(img):
    if img.shape[0] != 3:
        raise ValueError('La imagen debe tener 3 canales')
    weights = torch.tensor([0.2989, 0.5870, 0.1140], device=img.device)
    return torch.sum(img * weights.view(-1, 1, 1), dim=0, keepdim=True)

def circular_lowpass_kernel(cutoff, kernel_size, pad_to=0):
    pad_to = pad_to or kernel_size
    half = (kernel_size - 1) / 2.
    grid = torch.linspace(-half, half, kernel_size)
    x, y = torch.meshgrid(grid, grid)
    dist = torch.sqrt(x**2 + y**2)
    kernel = torch.sinc(dist * cutoff)
    kernel = kernel / kernel.sum()
    if pad_to > kernel_size:
        pad = (pad_to - kernel_size) // 2
        kernel = F.pad(kernel, [pad] * 4)
    return kernel

def random_mixed_kernels(
    kernel_list,
    kernel_prob,
    kernel_size=21,
    blur_sigma=0.1,
    blur_sigma_min=0.1,
    blur_sigma_max=10.0,
    pad_to=0
):
    kernel_type = np.random.choice(kernel_list, p=kernel_prob)
    pad_to = pad_to or kernel_size

    if kernel_type == 'iso':
        sigma = np.random.uniform(blur_sigma_min, blur_sigma_max)
        return _generate_isotropic_gaussian_kernel(kernel_size, sigma, pad_to)
    if kernel_type == 'aniso':
        sigma_x = np.random.uniform(blur_sigma_min, blur_sigma_max)
        sigma_y = np.random.uniform(blur_sigma_min, blur_sigma_max)
        rot = np.random.uniform(-np.pi, np.pi)
        return _generate_anisotropic_gaussian_kernel(kernel_size, sigma_x, sigma_y, rot, pad_to)

    return circular_lowpass_kernel(blur_sigma, kernel_size, pad_to)

def _generate_isotropic_gaussian_kernel(kernel_size=21, sigma=0.1, pad_to=0):
    pad_to = pad_to or kernel_size
    half = (kernel_size - 1) / 2.
    grid = torch.linspace(-half, half, kernel_size)
    x, y = torch.meshgrid(grid, grid)
    kernel = torch.exp(-(x**2 + y**2) / (2 * sigma**2))
    kernel = kernel / kernel.sum()
    if pad_to > kernel_size:
        pad = (pad_to - kernel_size) // 2
        kernel = F.pad(kernel, [pad] * 4)
    return kernel

def _generate_anisotropic_gaussian_kernel(kernel_size=21, sigma_x=0.1, sigma_y=0.1, rotation=0, pad_to=0):
    pad_to = pad_to or kernel_size
    half = (kernel_size - 1) / 2.
    grid = torch.linspace(-half, half, kernel_size)
    x, y = torch.meshgrid(grid, grid)

    cos_t = torch.cos(torch.tensor(rotation))
    sin_t = torch.sin(torch.tensor(rotation))
    x_r = cos_t * x - sin_t * y
    y_r = sin_t * x + cos_t * y

    kernel = torch.exp(-(x_r**2 / (2 * sigma_x**2) + y_r**2 / (2 * sigma_y**2)))
    kernel = kernel / kernel.sum()
    if pad_to > kernel_size:
        pad = (pad_to - kernel_size) // 2
        kernel = F.pad(kernel, [pad] * 4)
    return kernel
