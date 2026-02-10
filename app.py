import streamlit as st
import replicate
import os

st.title("🎬 AI Video Generator")

# Sidebar mein API Key lena
with st.sidebar:
    replicate_api = st.text_input('Replicate API Token daalein:', type='password')
    if not replicate_api:
        st.warning('App chalane ke liye Replicate API Token zaroori hai.')
    else:
        st.success('Token mil gaya!')

os.environ['REPLICATE_API_TOKEN'] = replicate_api

# Main interface
prompt = st.text_input("Aap kaisi video chahti hain? (English mein likhein):")

if st.button("Video Banayein"):
    if not replicate_api:
        st.error("Pehle sidebar mein API token daalein!")
    elif not prompt:
        st.error("Pehle kuch likhein!")
    else:
        with st.spinner("AI video bana raha hai... ismein 1-2 minute lag sakte hain."):
            try:
                # Video generation model chalana
                output = replicate.run(
    "anotherjesse/zeroscope-v2-xl:9f7434067175979f30f185399745c4369a451d0d0d822d3cb4d24119e7a177",
    input={"prompt": prompt}
                )
                # Video dikhana
                st.video(output[0])
                st.success("Aapki video taiyar hai!")
            except Exception as e:
                st.error(f"Error aaya: {e}")
