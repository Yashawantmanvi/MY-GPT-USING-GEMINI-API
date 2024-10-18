
import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get text-based responses
def get_gemini_text_response(question):
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    response = model.generate_content(question)
    return response.text

# Function to get image-based responses
def get_gemini_image_response(input_text, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input_text:
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="MY GPT")

st.header("MY GPT")

# Input for text-based Q&A
input_text = st.text_input("Input Prompt: ", key="input_text")
submit_text = st.button("Ask the question")

# Input for image-based response
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
submit_image = st.button("Tell me about the image")

# Handle text-based submission
if submit_text:
    if input_text:
        try:
            response = get_gemini_text_response(input_text)
            st.subheader("Response")
            st.write(response)
        except Exception as e:
            st.error(f"Error fetching response: {str(e)}")

# Handle image-based submission
if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

        if submit_image:
            input_text = st.text_input("Input for image description:", key="input_image_text")
            response = get_gemini_image_response(input_text, image)
            st.subheader("Response")
            st.write(response)
    except Exception as e:
        st.error(f"Error processing image: {str(e)}")