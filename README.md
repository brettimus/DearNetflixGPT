
Create venv

`python3 -m venv env`

`source env/bin/activate`

Install deps

`pip3 install streamlit langchain openai chromadb tiktoken`

Locally, I also needed to change urllib3 with `pip install urllib3==1.26.6` in order to run streamlit



`pip3 install watchdog`

## TODO - Add Gradio Tools

Tools for stable diffusion

`pip3 install gradio_tools`