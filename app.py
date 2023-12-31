import tensorflow
import dotenv
import transformers
from tensorflow import keras
from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
import langchain
from langchain import PromptTemplate, LLMChain, OpenAI

import requests
import os
import openai

import streamlit as st

HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")

load_dotenv(find_dotenv())


# img to text
def img2text(data):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

    text = image_to_text(data)[0]["generated_text"]

    print(text)
    return text


# llm
def generate_story(scenario):
    template = """
    You are a story teller;
    You can generate a short story based on a simple narrative, the story should be no more than 20 words;
    
    CONTEXT: {scenario}
    STORY: 
    """

    prompt = PromptTemplate(template=template, input_variables=["scenario"])

    story_llm = LLMChain(llm=OpenAI(model_name='gpt-3.5-turbo', temperature=1), 
                         prompt=prompt, verbose=True)

    story = story_llm.predict(scenario=scenario)

    print(story)
    return story


# txt to speech
def text2speech(message):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}
    payload = { "inputs": message }

    response = requests.post(API_URL, headers=headers, json=payload)
    with open('audio.flac', 'wb') as file:
        file.write(response.content)


def main():
    st.set_page_config(page_title="Image to Speech", page_icon="🤗")
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        print(uploaded_file)
        bytes_data = uploaded_file.getvalue()
        with open(uploaded_file.name, 'wb') as file:
            file.write(bytes_data)
        st.image(bytes_data, caption='Uploaded Image.', use_column_width=True)
        scenario = img2text(uploaded_file.name)
        story = generate_story(scenario)
        text2speech(story)
        
        with st.expander("scenario"):
            st.write(scenario)
        with st.expander("story"):
            st.write(story)
        
        st.audio('audio.flac')


if __name__ == '__main__':
    main()
