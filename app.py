import streamlit as st
from utils import generate_cold_email
from dotenv import load_dotenv
import os

load_dotenv()
together_api_key = os.getenv("TOGETHER_API_KEY")

st.set_page_config(page_title="Cold Email Generator", page_icon="📧", layout="centered")

# --- Header ---
st.title("📧 Cold Email Generator")
st.markdown("Generate personalized cold emails in seconds with AI.")

# --- Sidebar ---
st.sidebar.header("Configuration")
tone = st.sidebar.selectbox("Tone", ["Professional", "Friendly", "Persuasive", "Formal", "Casual"])
length_type = st.sidebar.selectbox("Email Length Based On", ["Paragraphs", "Lines"])
length_value = st.sidebar.slider(f"Number of {length_type}", 1, 10, 3)

# --- Form ---
with st.form("email_form"):
    name = st.text_input("Recipient Name", placeholder="e.g., Sarah")
    company = st.text_input("Company", placeholder="e.g., Acme Corp")
    product = st.text_input("Your Product/Service", placeholder="e.g., AI-Powered Analytics Tool")
    goal = st.text_input("Goal of the Email", placeholder="e.g., Schedule a product demo")

    submitted = st.form_submit_button("Generate Email")

    if submitted:
        if not together_api_key:
            st.error("Please set your Together API key in the `.env` file.")
        elif not all([name, company, product, goal]):
            st.warning("Please fill in all the fields.")
        else:
            with st.spinner("Generating email..."):
                email_text = generate_cold_email(
                    name=name,
                    company=company,
                    product=product,
                    goal=goal,
                    tone=tone,
                    length_type=length_type,
                    length_value=length_value
                )
                st.markdown("### ✉️ Generated Email")
                st.success("Email Generated Successfully!")
                st.code(email_text, language='markdown')
