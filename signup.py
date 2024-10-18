import streamlit as st

st.set_page_config(page_title="Sign Up - Relume", page_icon=":key:", layout="centered")

# Page style
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f0;
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
    .signup-container {
        background-color: #fff;
        padding: 40px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main container
with st.container():
    st.markdown('<div class="signup-container">', unsafe_allow_html=True)
    st.image("https://relume.io/static/images/logo.png", width=100)
    st.title("Sign up")

    # Signup form
    username = st.text_input("Username", placeholder="Username")
    email = st.text_input("Email", placeholder="Email address")
    password = st.text_input("Password", type="password", placeholder="Password")
    confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm Password")

    if st.button("Sign up"):
        # Implement your signup logic here
        if password == confirm_password:
            st.success("Signed up successfully!")
        else:
            st.error("Passwords do not match!")

    # Login link
    st.markdown('<a href="#" style="display: block; margin-top: 20px;">Already have an account? <strong>Log in</strong></a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
