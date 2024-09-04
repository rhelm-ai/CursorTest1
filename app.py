import streamlit as st
import requests
import base64

def load_css(file_name):
    with open(file_name, "r") as f:
        style = f.read()
    return f'<style>{style}</style>'

st.set_page_config(page_title="AI Business Name Generator", page_icon="🚀")

# Load CSS
css = load_css('styles/style.css')
st.markdown(css, unsafe_allow_html=True)

st.title("AI Business Name Generator")

prompt = st.text_area("Describe your business idea:")
if st.button("Generate Business Name"):
    response = requests.post("http://localhost:8000/generate_business_name", json={"prompt": prompt})
    business_name = response.json()["business_name"]
    st.subheader("Generated Business Name:")
    st.markdown(f'<div class="generated-name">{business_name}</div>', unsafe_allow_html=True)