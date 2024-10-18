from dotenv import load_dotenv

load_dotenv()  # Take environment variables from .env.

import streamlit as st
import os
import textwrap
from PIL import Image
import google.generativeai as genai
from IPython.display import Markdown

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Configure the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load OpenAI model and get text-based responses
def get_gemini_text_response(question):
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    response = model.generate_content(question)
    return response.text

# Function to load OpenAI model and get image-based responses
def get_gemini_image_response(input_text, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input_text:
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text
 
# Initialize our Streamlit app
st.set_page_config(page_title="Gemini Application")

st.header("Gemini Application")

# Input for text-based Q&A
input_text = st.text_input("Input Prompt: ", key="input_text")
submit_text = st.button("Ask the question")

# Input for image-based response
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
input_image_text = st.text_input("Describe the image: ", key="input_image_text")
submit_image = st.button("Tell me about the image")

# If the text-based submit button is clicked
if submit_text:
    response = get_gemini_text_response(input_text)
    st.subheader("The Response is")
    st.write(response)

# If the image-based submit button is clicked
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

    if submit_image:
        response = get_gemini_image_response(input_image_text, image)
        st.subheader("The Response is")
        st.write(response)
