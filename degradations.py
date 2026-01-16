import cv2
import math
import random
import numpy as np
import torch
from torch.nn import functional as F


def rgb_to_grayscale(img):
    if img.shape[0] != 3:
        raise ValueError("Input image must have 3 channels")
    weights = torch.tensor([0.2989, 0.5870, 0.1140], device=img.device).view(-1, 1, 1)
    return torch.sum(img * weights, dim=0, keepdim=True)


def random_add_gaussian_noise_pt(
    img,
    sigma_range=(0, 1.0),
    gray_prob=0,
    noise_gray_prob=0,
    clip=True,
    rounds=False
):
    noise_sigma = random.uniform(*sigma_range)

    if random.random() < gray_prob:
        img = rgb_to_grayscale(img)

    if random.random() < noise_gray_prob:
        noise = torch.randn(*img.shape[1:], device=img.device)
        noise = noise.unsqueeze(0).repeat(img.shape[0], 1, 1)
    else:
        noise = torch.randn_like(img)

    out = img + noise * noise_sigma

    if clip and rounds:
        return torch.clamp((out * 255).round(), 0, 255) / 255
    if clip:
        return torch.clamp(out, 0, 1)
    if rounds:
        return (out * 255).round() / 255
    return out


def random_add_poisson_noise_pt(
    img,
    scale_range=(0, 1.0),
    gray_prob=0,
    clip=True,
    rounds=False
):
    scale = random.uniform(*scale_range)

    if random.random() < gray_prob:
        img = rgb_to_grayscale(img)

    noise = torch.poisson(img * scale) / scale - img
    out = img + noise

    if clip and rounds:
        return torch.clamp((out * 255).round(), 0, 255) / 255
    if clip:
        return torch.clamp(out, 0, 1)
    if rounds:
        return (out * 255).round() / 255
    return out


def circular_lowpass_kernel(cutoff, kernel_size, pad_to=0):
    pad_to = pad_to or kernel_size
    assert pad_to >= kernel_size

    def sinc(x):
        if x == 0:
            return torch.tensor(1.0)
        x = x * math.pi
        return torch.sin(x) / x

    half = (kernel_size - 1) / 2
    grid = torch.linspace(-half, half, kernel_size)
    x, y = torch.meshgrid(grid, grid, indexing="ij")

    kernel = sinc(torch.sqrt(x ** 2 + y ** 2) * cutoff)
    kernel /= kernel.sum()

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
    pad_to = pad_to or kernel_size
    kernel_type = np.random.choice(kernel_list, p=kernel_prob)

    if kernel_type == "iso":
        sigma = np.random.uniform(blur_sigma_min, blur_sigma_max)
        return _iso_kernel(kernel_size, sigma, pad_to)

    if kernel_type == "aniso":
        return _aniso_kernel(
            kernel_size,
            np.random.uniform(blur_sigma_min, blur_sigma_max),
            np.random.uniform(blur_sigma_min, blur_sigma_max),
            np.random.uniform(-math.pi, math.pi),
            pad_to
        )

    return circular_lowpass_kernel(blur_sigma, kernel_size, pad_to)


def _iso_kernel(kernel_size, sigma, pad_to):
    half = (kernel_size - 1) / 2
    grid = torch.linspace(-half, half, kernel_size)
    x, y = torch.meshgrid(grid, grid, indexing="ij")

    kernel = torch.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))
    kernel /= kernel.sum()

    if pad_to > kernel_size:
        pad = (pad_to - kernel_size) // 2
        kernel = F.pad(kernel, [pad] * 4)

    return kernel


def _aniso_kernel(kernel_size, sigma_x, sigma_y, rotation, pad_to):
    half = (kernel_size - 1) / 2
    grid = torch.linspace(-half, half, kernel_size)
    x, y = torch.meshgrid(grid, grid, indexing="ij")

    cos_t = torch.cos(torch.tensor(rotation))
    sin_t = torch.sin(torch.tensor(rotation))

    xr = cos_t * x - sin_t * y
    yr = sin_t * x + cos_t * y

    kernel = torch.exp(
        -(xr ** 2 / (2 * sigma_x ** 2) + yr ** 2 / (2 * sigma_y ** 2))
    )
    kernel /= kernel.sum()

    if pad_to > kernel_size:
        pad = (pad_to - kernel_size) // 2
        kernel = F.pad(kernel, [pad] * 4)

    return kernel
