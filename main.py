import streamlit as st
import numpy
import torch

st.write("Success")
a = torch.Tensor([1])
st.write(type(a))

@st.cache()
def get_gen():
    gen = torch.jit.load("./scripted-generator.pt")
    return gen

gen = get_gen()