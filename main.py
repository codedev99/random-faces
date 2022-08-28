import streamlit as st
import numpy as np
import torch
from torch import nn

header = st.container()
interactive = st.container()
details = st.container()
display = st.container()

MODEL_PATH = "./scripted-generator.pt"

@st.cache()
def get_generator():
    generator = torch.jit.load(MODEL_PATH)
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
    generator = get_generator()
    c1, c2, c3 = st.columns([0.2, 1, 0.2])
    num_images = c2.slider("Number of random face images to generate?", min_value=4, max_value=16, value=4, step=4)

with display:
    noise = get_noise(num_images)
    tnoise = get_noise2(num_images)
    nfactor = c2.slider("Vary the input using random noise by what factor?", min_value=0., max_value=1., value=0., step=0.05)
    
    factor = nfactor * tnoise
    images = get_images(generator, noise, factor)

    cols = st.columns(4)
    for i in range(int(num_images/4)):
        for j in range(4):
            cols[j].image(images[i*4+j], use_column_width=True)