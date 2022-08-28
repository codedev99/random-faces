import streamlit as st
import numpy
import torch

st.write("Success")
a = torch.Tensor([1])
st.write(type(a))
gen = torch.jit.load("./scripted-generator.pt")

@st.cache()
def get_noise(num_images):
    noise = torch.randn(num_images, 128)
    return noise

noise = get_noise()
st.write(noise[0,0].item())