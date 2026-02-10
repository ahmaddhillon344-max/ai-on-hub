import streamlit as st
from openai import OpenAI

# App ka Title
st.title("🤖 Mera Pehla AI Chatbot")

# Sidebar mein API Key mangna
with st.sidebar:
    api_key = st.text_input("OpenAI API Key daalein:", type="password")

if api_key:
    client = OpenAI(api_key=api_key)
    
    # User se sawaal lena
    user_query = st.text_input("AI se kuch bhi poochein:")
    
    if st.button("Jawab Den"):
        if user_query:
            # AI Model ko call karna
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_query}]
            )
            st.success(response.choices[0].message.content)
else:
    st.info("App chalane ke liye sidebar mein OpenAI API Key enter karein.")
