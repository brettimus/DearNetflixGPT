import streamlit as st
from langchain import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
# from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferMemory
# from gradio_tools import (StableDiffusionTool, ImageCaptioningTool, StableDiffusionPromptGeneratorTool)
# from gradio_tools import (StableDiffusionTool, ImageCaptioningTool, StableDiffusionPromptGeneratorTool, TextToVideoTool)

from generate_image import generate_image

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
memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')

# LLMs
llm = OpenAI(temperature=0.7)

topic_chain = LLMChain(llm=llm, prompt=topic_template, verbose=True, output_key='pitch')

script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script')

sequential_chain = SequentialChain(chains=[topic_chain, script_chain], input_variables=['topic'], output_variables=['pitch', 'script'], verbose=True)

# Agent setup - 
# NOT WORKING, PROBABLY NEED TO HOST A STABLE DIFFUSION MODEL MYSELF (?)
# tools = [
#     StableDiffusionTool().langchain,
#     ImageCaptioningTool().langchain,
#     StableDiffusionPromptGeneratorTool().langchain, 
#     # TextToVideoTool().langchain
# ]
# image_agent = initialize_agent(tools=tools, memory=memory, agent="dearnetflix-hero-image", verbose=True)


# App
st.title('"Dear Netflix..."')

st.write('*Provide a topic or description for a Netflix series you would like to make, and AI will write the pitch and first episode for you!*')

prompt = st.text_input('Add the topic for your series below. Write either a single word (e.g., socks), or include as much detail as you see fit')
st.divider()

if prompt:
    response = sequential_chain({ 'topic': prompt })
    pitch = response['pitch']
    st.subheader('Here are your pitch and script!')
    image_url = generate_image(pitch)
    # st.write(image_url)
    st.markdown(f"![promotional image for {prompt}]({image_url})")
    st.write(pitch)
    st.write(response['script'])

    # GRADIO TOOLS IS NOT WORKING
    #
    # image_output = image_agent.run(input=("Please create a Netflix series promotional image for the following Netflix series: {pitch}"
    #                       "but improve my prompt prior to using an image generator."
    #                       "Please caption the generated image using the improved prompt" #   "Please caption the generated image and create a video for it using the improved prompt."
    #             ))
else:
    st.subheader('Your pitch and script will appear below:')

