import openai

from langchain import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

def generate_image(user_pitch):
    """
    Process an image request and generate a response.
    Args:
        pitch (str): Input text message.
    Returns:
        str: The generated response.
    """
    prompt_template_text = """
        Please create a Netflix series promotional image for a Netflix series that they are pitching. 
        The user wants an image from you. You will get the image from DALL-E / Stable Diffusion.
        Based on the pitch do you have a good idea for the promotional image?
        If so create an awesome prompt for DALL-E. It should create a prompt relevant to what the user is looking for.
        If it is not clear what the image should be about; return this exact message 'false'.
        Here is the pitch for the series: {pitch}
        Prompt for image:
    """
    image_prompt_template = PromptTemplate(input_variables=["pitch"], template=prompt_template_text)

    llm = OpenAI(temperature=0.4)

    image_prompt_chain = LLMChain(
        llm=llm,
        prompt=image_prompt_template,
        verbose=True,
        memory=ConversationBufferMemory(),
    )

    prompt_text = image_prompt_chain.predict(pitch=user_pitch)

    if prompt_text == "false":
        output = "Please provide more details about the image you're looking for."
    else:
        try:
            response = openai.Image.create(prompt=prompt_text, n=1, size="256x256")
            deissue = False
            image = response["data"][0]["url"]
        except:
            deissue = True

        if deissue:
            output = "Your request was rejected. Sorry bout that. Did you try to do something potentially harmful?"
        else:
            output = image

    return output