# app.py
import streamlit as st
from recommender import load_anime_data, recommend_anime
from chatbot import chat_with_gpt

df = load_anime_data()
st.title("Anime Recommender Chatbot")

user_input = st.text_input("Tell me an anime you like:")
if st.button("Recommend"):
    recs = recommend_anime(user_input, df)
    st.write(chat_with_gpt(user_input, recs))
