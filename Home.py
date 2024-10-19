import streamlit as st
from pymongo import MongoClient
import hashlib
import card  # Import your card.py module

from pymongo.errors import ServerSelectionTimeoutError

try:
    client = pymongo.MongoClient(mongodb://localhost:27017/, serverSelectionTimeoutMS=5000)
    db = client["ninja_gpt"]
    # Test the connection
    client.server_info()  # Will throw an exception if not connected
    print("MongoDB connection successful!")
except ServerSelectionTimeoutError as err:
    print(f"Connection failed: {err}")

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["ninja_gpt"]
users_collection = db["users"]

# Helper functions
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(email, password):
    hashed_password = hash_password(password)
    users_collection.insert_one({"email": email, "password": hashed_password})

def authenticate_user(email, password):
    hashed_password = hash_password(password)
    user = users_collection.find_one({"email": email, "password": hashed_password})
    return user is not None

# Set Streamlit page config
st.set_page_config(page_title="MY GPT", page_icon="🤖", layout="wide")

# Styles and main screen navigation bar setup
st.markdown("""
    <style>
    .nav-bar {
        display: flex;
        justify-content: center;
        background-color: #004080;
        padding: 10px 0;
    }
    .nav-bar a {
        text-decoration: none;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        margin: 0 10px;
        border-radius: 5px;
        transition: background-color 0.3s;
    }
    .nav-bar a:hover {
        background-color: #0059b3;
    }
    .center-box {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 70vh;
    }
    .form-box {
        background-color: #fff;
        padding: 40px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    .stButton button {
        width: 100%;
        background-color: #000;
        color: #fff;
        border: none;
        padding: 10px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #333;
    }
    .stTextInput>div>input {
        padding: 10px;
        font-size: 16px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Main screen navigation bar display
st.markdown("""
    <div class="nav-bar">
        <a href="?nav=Home">Home</a>
        <a href="?nav=SignUp">Sign Up</a>
        <a href="?nav=Login">Login</a>
        <a href="?nav=About">About</a>
    </div>
""", unsafe_allow_html=True)

# Get the navigation state from query parameters
query_params = st.query_params
nav = query_params.get("nav", "Home")

# Home Page
if nav == "Home":
    st.title("Welcome to MY GPT 🤖")
    st.write("""
  
    MY GPT is an advanced AI project utilizing the Gemini API to deliver a versatile and powerful user experience. 
    
    -> It excels in responding to text-based queries, providing accurate and contextually relevant answers. Additionally, 
    
    -> It has a features that has ability to chat with multiple PDFs, enabling users to interact with and extract information from various documents seamlessly. 
    
    -> The project also incorporates image recognition capabilities, offering detailed descriptions of uploaded images. 
    
    -> Another notable feature is its invoice extractor, which supports multi-language invoices and allows users to engage in a conversational interface for efficient data extraction from uploaded invoices.
    
     MY GPT demonstrates the versatile capabilities of Generative AI in various applications.
     
    """)

# SignUp Page

elif nav == "SignUp":
    # Page style
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f0f0;
        }
       
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Main container
    with st.container():
        st.markdown('<div class="signup-container">', unsafe_allow_html=True)
        st.title("Sign up")

        # Signup form
        email = st.text_input("Email", placeholder="Email address")
        password = st.text_input("Password", type="password", placeholder="Password")
        confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm Password")

        if st.button("Sign up"):
            if password == confirm_password:
                create_user(email, password)
                st.success("Account created successfully! Please login.")
            else:
                st.error("Passwords do not match!")

        st.markdown('<a href="?nav=Login" style="display: block; margin-top: 20px;">Already have an account? <strong>Log in</strong></a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Login Page
elif nav == "Login":
    # Page style
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f0f0;
        }
       
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Main container
    with st.container():
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.title("Log in")

        # Login form
        email = st.text_input("Email", placeholder="Email address")
        password = st.text_input("Password", type="password", placeholder="Password")

        if st.button("Log in"):
            if authenticate_user(email, password):
                st.session_state.logged_in = True  # Set session state for logged in user
                st.session_state.user = email
            else:
                st.error("Invalid credentials")

        st.markdown('<a href="#" style="display: block; margin-top: 10px;">Forgot password?</a>', unsafe_allow_html=True)
        st.markdown('<a href="?nav=SignUp" style="display: block; margin-top: 20px;">Don\'t have an account? <strong>Sign up</strong></a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# About Page
elif nav == "About":
    st.title("About MY GPT™")
    st.write("""

 This project harnesses the power of Generative AI 
 Provides a versatile tool capable of handling a wide range of tasks.
 
 It including text-based queries.
  
 Interacting with multiple PDFs.
  
 Performing image recognition, and extracting information from invoices in multiple languages.

The primary aim of MY GPT is to offer a seamless and intuitive interface that leverages advanced AI capabilities to assist users in various domains, from document management to automated responses.
Our platform is designed to enhance productivity and provide a user-friendly experience.

Contact Us  For more information about MY GPT™, 

please visit our official website or reach out to us via email at info@mygpt.com.

You can also follow us on social media:

LinkedIn
Twitter
Facebook
    
""")

# Check if logged in and redirect to card.py
if st.session_state.get("logged_in"):
    st.title(f"Welcome, {st.session_state.user}!")
    st.write("Redirecting to service page...")
    card.main()  # Call main function from card.py to display its content
