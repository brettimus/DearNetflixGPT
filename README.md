## Description

A proof of concept using langchain to create a pitch for a tv series from a short user prompt.

Still very much WIP.

## Try it out locally

Create venv and install deps

```sh
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
# if installing from requirements.txt isn't working, try:
pip3 install streamlit langchain openai chromadb tiktoken urllib3==1.26.6
# if you want to speed up reloading, also run
pip3 install watchdog
```

Add secrets to `.streamlit/secrets.toml`

```sh
echo OPENAI_API_KEY="yyy" >> .streamlit/secrets.toml
```

After that, you can run the app

```sh
# While in virtual environment
streamlit run app.py
```


## TODO - Add Gradio Tools

Gradio just released some tools for doing things stable diffusion

`pip3 install gradio_tools`

however, these rely on hugging face hosted stable diffusion models and some do not load reliably, so i couldn't get their example from the docs to work

## Inspiration

I got the Dall-E thing to work by looking at this repo: https://github.com/mortium91/langchain-assistant/blob/main/app/chat_handler.py