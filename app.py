from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai


load_dotenv() # load all the env variables from .env
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini Pro Vision
model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # read file into bytes
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    

# init streamlit page
st.set_page_config(page_title="AI-Powered Multilanguage Invoice Extractor")

st.header("AI-Powered Multilanguage Invoice Extractor")
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image/file of the invoice", type=["jpg", "png", "pdf"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="uploaded Image.", use_column_width=True)
    
submit=st.button("Tell me about the invoice")

input_prompt ="""
You are en expert in understanding invoices. We will upload an image as invoice and 
you will have to answer any questions based on the uploaded invoice image
"""

if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The Response is")
    st.write(response)
    