# configuración e instalación del proyecto real-esrgan
%%capture

# verificar gpu disponible
!nvidia-smi

# clonar repositorio desde github
!git clone https://github.com/xinntao/Real-ESRGAN.git
%cd Real-ESRGAN

# instalar dependencias principales
!pip install basicsr
!pip install facexlib
!pip install gfpgan
!pip install -r requirements.txt
!python setup.py develop

# importar librerías necesarias
import shutil
from tqdm import tqdm
import os
import shutil, sys
import re
import io
import IPython.display
import numpy as np
import PIL.Image
from google.colab import files
import shutil

# url del modelo gfpgan
new_model_path = 'https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth'

# archivo de inferencia de real-esrgan
filename = '/content/Real-ESRGAN/inference_realesrgan.py'
with open(filename, 'r') as f:
    script_content = f.read()

# reemplazar ruta del modelo
new_script_content = re.sub(
    r"(model_path\s*=\s*[\"\']).*?([\"\'])",
    rf"\g<1>{new_model_path}\g<2>",
    script_content
)

# guardar cambios
with open(filename, 'w') as f:
    f.write(new_script_content)

# corregir compatibilidad con torchvision
!sed -i 's/from torchvision.transforms.functional_tensor import rgb_to_grayscale/from torchvision.transforms.functional import rgb_to_grayscale/' /usr/local/lib/python3.10/dist-packages/basicsr/data/degradations.py

# código de degradaciones modificado
degradations_code = '''import cv2
import math
import numpy as np
import random
import torch
from torch.nn import functional as F

def random_add_gaussian_noise_pt(img, sigma_range=(0, 1.0), gray_prob=0, noise_gray_prob=0, clip=True, rounds=False):
    noise_sigma = random.uniform(*sigma_range)

    if random.random() < gray_prob:
        img = rgb_to_grayscale(img)

    if random.random() < noise_gray_prob:
        noise = torch.randn(*img.shape[1:], device=img.device) * noise_sigma
        noise = noise.unsqueeze(0).repeat(img.shape[0], 1, 1)
    else:
        noise = torch.randn_like(img) * noise_sigma

    out = img + noise

    if clip and rounds:
        out = torch.clamp((out * 255.0).round(), 0, 255) / 255.
    elif clip:
        out = torch.clamp(out, 0, 1)
    elif rounds:
        out = (out * 255.0).round() / 255.

    return out

def random_add_poisson_noise_pt(img, scale_range=(0, 1.0), gray_prob=0, clip=True, rounds=False):
    scale = random.uniform(*scale_range)

    if random.random() < gray_prob:
        img = rgb_to_grayscale(img)

    noise = torch.poisson(img * scale) / scale - img
    out = img + noise

    if clip and rounds:
        out = torch.clamp((out * 255.0).round(), 0, 255) / 255.
    elif clip:
        out = torch.clamp(out, 0, 1)
    elif rounds:
        out = (out * 255.0).round() / 255.

    return out

def rgb_to_grayscale(img):
    if img.shape[0] != 3:
        raise ValueError('input image must have 3 channels')
    rgb_weights = torch.tensor([0.2989, 0.5870, 0.1140], device=img.device)
    grayscale = torch.sum(img * rgb_weights.view(-1, 1, 1), dim=0, keepdim=True)
    return grayscale
'''

# detectar versión de python
python_version = f"python{sys.version_info.major}.{sys.version_info.minor}"

# ruta del archivo degradations
degradations_path = f'/usr/local/lib/{python_version}/dist-packages/basicsr/data/degradations.py'

# crear respaldo
!cp -n {degradations_path} {degradations_path}.backup

# escribir nuevo archivo
with open(degradations_path, 'w') as f:
    f.write(degradations_code)
