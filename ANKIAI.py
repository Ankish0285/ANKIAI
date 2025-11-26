import google.generativeai as genai
import streamlit as st
import pandas as pd 

#______________logo_____________________
col1, col2 = st.columns([6, 1])
with col2:
    st.image(r"c:/users/ANKISH KUMAR/Downloads/ANKIAI.png", width=80)



#_______________dashboard create ______
with st.sidebar:
    st.title("MENU")
    st.button("New chat")
    st.button("Refresh")
    st.button("History")
    st.button("Settings")
    st.button("Help")
    st.button("Profile")
    st.button("About")
    st.info("Dashboard version 1.0 created by Ankish")

st.title("ANKIAI")
st.text("WELCOME TO ANKIAI DASHBOARD")


#______________chatbot create__________
key = "enter your api_key"
genai.configure(api_key=key)

model = genai.GenerativeModel("gemini-2.5-flash")


#______________user input section__________
input_col, send_col = st.columns([10, 1])

with input_col:
    user_input = st.text_input("Ask me anything...... ", key="input",placeholder="type your question...")

#______________upload button_________________
with st.expander("+"):
    st.subheader("upload file")
    uploaded = st.file_uploader("", type=["png", "jpg", "jpeg", "pdf", "documents"], label_visibility="collapsed")
    if uploaded:
        st.success("file uploaded successfully")

with send_col:
    send = st.button("➤")

#___________press enter toauto send _________
enter_pressed = user_input != ""

if send or enter_pressed:
    if user_input.strip() != "":

        with st.spinner("Generating response..."):
            response = model.generate_content(user_input)
        st.success("Bot Response:")
        st.write(response.text)

st.success("Dashboard Loaded Successfully!")