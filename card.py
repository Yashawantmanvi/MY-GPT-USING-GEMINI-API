import streamlit as st

def main():
    # Page title
    st.title("Our Services to Ease Your Life")

    # Custom CSS styles
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f0f0; /* Light gray background */
            padding: 20px; /* Add padding for content */
        }
        .navbar {
            background-color: #333333;
            padding: 10px 0;
            margin-bottom: 20px;
            display: flex;
            justify-content: center;
        }
        .navbar a {
            color: #ffffff;
            text-decoration: none;
            padding: 10px 20px;
            margin: 0 10px;
            border-radius: 10px;
        }
        .navbar a:hover {
            background-color: #555555;
        }
        .service-card {
            background-color: lavender; /* Lavender color */
            color: #333333; /* Dark text */
            border-radius: 15px; /* Rounded corners */
            padding: 15px;
            margin: 25px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); /* Shadow effect */
            transition: transform 0.3s ease;
            width: 500px; /* Adjusted width */
        }
        .service-card:hover {
            transform: translateY(-5px); /* Move up on hover */
            box-shadow: 0 12px 20px rgba(0, 0, 0, 0.4); /* Increase shadow on hover */
        }
        </style>
        """
    , unsafe_allow_html=True)

    # Navigation bar
    st.markdown(
        """
        <div class="navbar">
            <a href="?nav=Home">Home</a>
            <a href="?nav=Services">Services</a>
            <a href="?nav=About">About</a>
            <a href="?nav=Contact">Contact</a>
        </div>
        """
    , unsafe_allow_html=True)

    # Service cards
    st.markdown("<h3> Choose  services from SideBar to get started</h3>", unsafe_allow_html=True)
    st.markdown("<h2>Our Services</h2>", unsafe_allow_html=True)

    services = {
        "AI Chatbot": "Advanced AI-powered chatbot for interactive customer support.",
        "ChatWithPdf": "If you have multiple PDFs, you can use this.",
        "VisionPro": "Upload an image here and ask whatever you want about that image.",
        "Invoice Extractor": "Supports multiple languages."
    }

    for service, description in services.items():
        
        st.markdown(
            f"""
            <div class="service-card">
                <h3>{service}</h3>
                <p>{description}</p>
            </div>
            """
        , unsafe_allow_html=True)

if __name__ == "__main__":
    main()
