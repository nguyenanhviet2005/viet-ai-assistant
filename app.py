import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Viet AI Assistant")

mode = st.selectbox("Mode", ["Technical", "Business Strategy"])

if mode == "Technical":
    system_prompt = "You are a senior ASTM consultant specializing in concrete floor flatness."
else:
    system_prompt = "You are a strategic advisor helping grow a concrete flooring business."

user_input = st.text_area("Ask your assistant:")

if st.button("Submit"):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    st.write(response.choices[0].message.content)
