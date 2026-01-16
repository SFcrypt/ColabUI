import cv2, math, random, torch, numpy as np
from torch.nn import functional as F

def random_add_gaussian_noise_pt(img, sigma_range=(0,1.0), gray_prob=0, noise_gray_prob=0, clip=True, rounds=False):
    noise_sigma = random.uniform(*sigma_range)
    if random.random() < gray_prob: img = rgb_to_grayscale(img)
    noise = (torch.randn(*img.shape[1:], device=img.device).unsqueeze(0).repeat(img.shape[0],1,1)
             if random.random() < noise_gray_prob else torch.randn_like(img)) * noise_sigma
    out = img + noise
    if clip and rounds: return torch.clamp((out*255).round(),0,255)/255
    if clip: return torch.clamp(out,0,1)
    if rounds: return (out*255).round()/255
    return out

def random_add_poisson_noise_pt(img, scale_range=(0,1.0), gray_prob=0, clip=True, rounds=False):
    scale = random.uniform(*scale_range)
    if random.random() < gray_prob: img = rgb_to_grayscale(img)
    out = img + (torch.poisson(img*scale)/scale - img)
    if clip and rounds: return torch.clamp((out*255).round(),0,255)/255
    if clip: return torch.clamp(out,0,1)
    if rounds: return (out*255).round()/255
    return out

def rgb_to_grayscale(img):
    if img.shape[0] != 3: raise ValueError('Input image must have 3 channels')
    w = torch.tensor([0.2989,0.5870,0.1140], device=img.device).view(-1,1,1)
    return torch.sum(img*w, dim=0, keepdim=True)

def circular_lowpass_kernel(cutoff, kernel_size, pad_to=0):
    pad_to = pad_to or kernel_size
    assert pad_to >= kernel_size
    def sinc(x): return torch.tensor(1.) if x==0 else torch.sin(x*math.pi)/(x*math.pi)
    g = torch.linspace(-(kernel_size-1)/2, (kernel_size-1)/2, kernel_size)
    x,y = torch.meshgrid(g,g)
    k = sinc(torch.sqrt(x**2+y**2)*cutoff); k /= k.sum()
    if pad_to>kernel_size: k = F.pad(k,[(pad_to-kernel_size)//2]*4)
    return k

def random_mixed_kernels(kernel_list, kernel_prob, kernel_size=21, blur_sigma=0.1,
                          blur_sigma_min=0.1, blur_sigma_max=10.0, pad_to=0):
    pad_to = pad_to or kernel_size
    t = np.random.choice(kernel_list, p=kernel_prob)
    if t=='iso': return _iso(kernel_size, np.random.uniform(blur_sigma_min,blur_sigma_max), pad_to)
    if t=='aniso': return _aniso(kernel_size,
                                  np.random.uniform(blur_sigma_min,blur_sigma_max),
                                  np.random.uniform(blur_sigma_min,blur_sigma_max),
                                  np.random.uniform(-np.pi,np.pi), pad_to)
    return circular_lowpass_kernel(blur_sigma, kernel_size, pad_to)

def _iso(k,s,p):
    g = torch.linspace(-(k-1)/2,(k-1)/2,k)
    x,y = torch.meshgrid(g,g)
    k = torch.exp(-(x**2+y**2)/(2*s**2)); k/=k.sum()
    return F.pad(k,[(p-k.shape[0])//2]*4) if p>k.shape[0] else k

def _aniso(k,sx,sy,r,p):
    g = torch.linspace(-(k-1)/2,(k-1)/2,k)
    x,y = torch.meshgrid(g,g)
    c,s = torch.cos(torch.tensor(r)), torch.sin(torch.tensor(r))
    xr,yr = c*x-s*y, s*x+c*y
    k = torch.exp(-(xr**2/(2*sx**2)+yr**2/(2*sy**2))); k/=k.sum()
    return F.pad(k,[(p-k.shape[0])//2]*4) if p>k.shape[0] else k
