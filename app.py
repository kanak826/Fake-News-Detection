import streamlit as st
import string
import pickle

# LOAD MODEL

model = pickle.load(
    open("model.pkl", "rb")
)

vectorizer = pickle.load(
    open("vectorizer.pkl", "rb")
)

# CLEAN FUNCTION

def clean_text(text):

    text = text.lower()

    text = ''.join(
        char for char in text
        if char not in string.punctuation
    )

    return text

# GUI

st.title("Fake News Detection System")

news_input = st.text_area(
    "Enter News Text"
)

# PREDICTION

if st.button("Predict"):

    cleaned_news = clean_text(news_input)

    vector_input = vectorizer.transform(
        [cleaned_news]
    )

    prediction = model.predict(
        vector_input
    )

    if prediction[0] == 0:

        st.error("Fake News")

    else:

        st.success("Real News")