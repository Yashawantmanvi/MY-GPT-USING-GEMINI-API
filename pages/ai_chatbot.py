from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from pymongo import MongoClient

# Configure the Google Generative AI with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Configure MongoDB client
mongo_client = MongoClient(os.getenv("MONGODB_URI"))
db = mongo_client['chat_db']
collection = db['chat_history']

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize Streamlit app
st.set_page_config(page_title="Q&A ", layout="wide")

# Function to save chat history to MongoDB
def save_chat_history(chat_history):
    collection.insert_one({"chat_history": chat_history})

# Function to load chat histories from MongoDB
def load_chat_histories():
    return list(collection.find())

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Sidebar for dark mode toggle and chat history
with st.sidebar:
    dark_mode_toggle = st.checkbox("Dark Mode", key="dark_mode")

    st.subheader("Chat History")
    chat_histories = load_chat_histories()
    for idx, chat_doc in enumerate(chat_histories):
        if st.button(f"Chat {idx+1}"):
            st.session_state['chat_history'] = chat_doc['chat_history']

# Custom CSS for colorful fonts and modern look
custom_css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    body {
        font-family: 'Roboto', sans-serif;
        background-color: #f0f2f6;
        color: #333333;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        color: #333333;
        border-radius: 8px;
    }
    .sidebar .sidebar-content h3 {
        font-size: 1.5rem;
        margin-bottom: 10px;
    }
    .main-content {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .header {
        text-align: center;
        margin-bottom: 40px;
    }
    .header h1 {
        font-size: 2.5rem;
        color: #007BFF;
    }
    .header p {
        font-size: 1.25rem;
        color: #555555;
    }
    .question-section {
        margin-top: 40px;
    }
    .question-section h2 {
        font-size: 2rem;
        color: #007BFF;
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        font-size: 0.875rem;
        color: #555555;
    }
    .stTextInput, .stButton, .stSubheader, .stHeader {
        color: #007BFF;
    }
    </style>
    """

dark_mode_css = """
    <style>
    body, .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    .sidebar .sidebar-content {
        background-color: #212529;
        color: #fafafa;
    }
    .sidebar .sidebar-content h3 {
        color: #fafafa;
    }
    .stTextInput, .stButton, .stSubheader, .stHeader {
        color: #1E90FF;
    }
    .main-content {
        background-color: #212529;
        color: #fafafa;
    }
    .header h1 {
        color: #1E90FF;
    }
    .header p {
        color: #B0C4DE;
    }
    .question-section h2 {
        color: #1E90FF;
    }
    .footer {
        color: #B0C4DE;
    }
    .chat-history .role-user {
        color: #1E90FF;
    }
    .chat-history .role-bot {
        color: #B0C4DE;
    }
    </style>
    """

# Apply styles based on dark mode toggle
if st.session_state.dark_mode:
    st.markdown(dark_mode_css, unsafe_allow_html=True)
else:
    st.markdown(custom_css, unsafe_allow_html=True)

st.header("MY GPT")

# Input for user query
input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# Handle the response and update chat history
if submit and input_text:
    response = get_gemini_response(input_text)
    st.session_state['chat_history'].append(("You", input_text))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
    save_chat_history(st.session_state['chat_history'])

# Display the current chat history in the main area
st.subheader("Current Chat History")
st.markdown('<div class="chat-history">', unsafe_allow_html=True)
for role, text in st.session_state['chat_history']:
    role_class = "role-user" if role == "You" else "role-bot"
    st.markdown(f'<p class="{role_class}">{role}: {text}</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>Powered by Generative AI </p>
    </div>
    """, unsafe_allow_html=True)
