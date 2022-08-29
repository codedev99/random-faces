"""
Generate synthetic 48x48x3 face images using random normal noise.

Display an nx4 grid of face images generated using a DCGAN generator. Vary the output
face images and see the transitions, by varying the input to the DCGAN. This is done
by multiplying the input noise by a secondary noise through varying degrees.
"""

import streamlit as st
import numpy as np
import torch
from torch import nn
import io
import copy

header = st.container()
interactive = st.container()
details = st.container()
display = st.container()

MODEL_PATH = "./scripted-generator.pt"

@st.cache()
def get_bytesobj():
    # stores script model as buffer for faster jit.load
    with open(MODEL_PATH, 'rb') as f:
        buffer = io.BytesIO(f.read())
    return buffer

def get_generator(bytesobj):
    generator = torch.jit.load(bytesobj)
    return generator

@st.cache()
def get_noise(num_images):
    noise = torch.randn(num_images, 128)
    return noise

@st.cache()
def get_noise2(num_images):
    noise = torch.randn(num_images, 128)
    return noise

def get_images(generator, noise, factor):
    noise = noise + factor
    images = generator(noise)
    images = images.detach()
    images = (images.permute((0,2,3,1)) + 1) * 127.5
    images = images.numpy().astype(np.uint8)
    return images

with header:
    st.title("Random Faces")
    st.text("Welcome to the Random Faces app. This project generates synthetic 48x48 face images from random noise.")

with interactive:
    bytesobj = copy.copy(get_bytesobj()) # clone buffer, to retain for reuse
    generator = get_generator(bytesobj)
    c1, c2, c3 = st.columns([0.2, 1, 0.2])
    num_images = c2.slider("Number of random face images to generate?", min_value=4, max_value=16, value=4, step=4)

with display:
    noise = get_noise(num_images)
    tnoise = get_noise2(num_images)
    nfactor = c2.slider("Vary the input using random noise by what factor?", min_value=0., max_value=1., value=0., step=0.05)
    
    # vary the input noise using the secondary 'tnoise'
    factor = nfactor * tnoise
    images = get_images(generator, noise, factor)

    cols = st.columns(4)
    for i in range(int(num_images/4)):
        for j in range(4):
            cols[j].image(images[i*4+j], use_column_width=True)