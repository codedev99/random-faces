import streamlit as st
import numpy
import torch

st.write("Success")
a = torch.Tensor([1])
st.write(type(a))
gen = torch.jit.load("./scripted-generator.pt")