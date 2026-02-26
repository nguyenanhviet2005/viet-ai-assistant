import streamlit as st
from openai import OpenAI

# ==============================
# PAGE CONFIG (Quan trọng cho PWA)
# ==============================
st.set_page_config(
    page_title="Viet AI Assistant",
    page_icon="static/icon-192.png",
    layout="centered"
)

# Gắn manifest cho Android
st.markdown(
    """
    <link rel="manifest" href="/static/manifest.json">
    """,
    unsafe_allow_html=True
)

# ==============================
# OPENAI CLIENT
# ==============================
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ==============================
# UI
# ==============================
st.title("Viet AI Assistant")

st.markdown("AI assistant for floor consulting and business development")

mode = st.selectbox(
    "Select Mode",
    ["Technical (Consultant)", "Business Strategy"]
)

if mode == "Technical (Consultant)":
    system_prompt = "You are a senior ASTM consultant specializing in concrete floor flatness and F-number standards."
else:
    system_prompt = "You are a strategic advisor helping grow a concrete flooring business globally."

user_input = st.text_area("Ask your assistant:")

if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ]
            )

            st.success("Response:")
            st.write(response.choices[0].message.content)


