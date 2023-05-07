import os

import streamlit as st
from langchain.llms import OpenAI


st.title('Untitled...')
prompt = st.text_input('Plug in your prompt here...')

