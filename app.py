from dotenv import load_dotenv

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
# from langchain.agents import initialize_agent
# from langchain.memory import ConversationBufferMemory

# from gradio_tools import (StableDiffusionTool, ImageCaptioningTool, StableDiffusionPromptGeneratorTool, TextToVideoTool)

load_dotenv()

# Prompt Templates
topic_template = PromptTemplate(
    input_variables=['topic'],
    template='You are an experienced writer and showrunner in the entertainment industry. Help me write a pitch to Netflix for a series about the following: {topic}.',
)

script_template = PromptTemplate(
    input_variables=['pitch'],
    template='You are writing the first episode for a Netflix series, here is the pitch for the series: {pitch}. Give an example script of a scene from the first episode of this series.',
)

# Memory
# memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')


# LLMs
llm = OpenAI(temperature=0.7)
topic_chain = LLMChain(llm=llm, prompt=topic_template, verbose=True, output_key='pitch')
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script')
sequential_chain = SequentialChain(chains=[topic_chain, script_chain],input_variables=['topic'], output_variables=['pitch', 'script'], verbose=True)

# Agent setup
# tools = [
#     StableDiffusionTool().langchain,
#     ImageCaptioningTool().langchain,
#     StableDiffusionPromptGeneratorTool().langchain, 
#     # TextToVideoTool().langchain
# ]

# App
st.title('"Dear Netflix..."')

st.write('*Provide a topic or description for a Netflix series you would like to make, and AI will write the pitch and first episode for you!*')

prompt = st.text_input('Add the topic for your series below. Write either a single word (e.g., socks), or include as much detail as you see fit')
st.divider()

if prompt:
    response = sequential_chain({ 'topic': prompt })
    st.subheader('Here are your pitch and script!')
    st.write(response['pitch'])
    st.write(response['script'])
else:
    st.subheader('Your pitch and script will appear below:')

