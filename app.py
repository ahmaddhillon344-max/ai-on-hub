import streamlit as st
import replicate
import os

st.title("🎬 AI Video Generator")

# Sidebar for API Key
with st.sidebar:
    replicate_api = st.text_input('Replicate API Token daalein:', type='password')
    if not replicate_api:
        st.warning('Pehle Token daalein.')

os.environ['REPLICATE_API_TOKEN'] = replicate_api

prompt = st.text_input("Aap kaisi video chahti hain? (English mein likhein):")

if st.button("Video Banayein"):
    if not replicate_api:
        st.error("Sidebar mein API token paste karein!")
    else:
        with st.spinner("AI video bana raha hai..."):
            try:
                # Naya aur stable model version
                output = replicate.run(
                    "anotherjesse/zeroscope-v2-xl:9f7434067175979f30f185399745c4369a451d0d0d822d3cb4d24119e7a177",
                    input={"prompt": prompt}
                )
                st.video(output[0])
                st.success("Video taiyar hai!")
            except Exception as e:
                st.error(f"Error: {e}")
