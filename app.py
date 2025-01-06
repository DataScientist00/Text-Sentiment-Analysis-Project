import streamlit as st
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the pickled tokenizer and model
tokenizer = pickle.load(open('tokenizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


# Streamlit app
st.title("🌟 Text Sentiment Analysis 🌟")

# User input
user_input = st.text_area("Enter your text:", "")

# Process input and make prediction if submitted
if st.button("🔍 Analyze Sentiment"):
    if user_input.strip():
        # Convert text input to tokens using the tokenizer
        tokenized_input = tokenizer.texts_to_sequences([user_input])
        
        # Padding input to match the expected input length for the model
        max_len = 200  # Set this to the same as used during training
        padded_input = pad_sequences(tokenized_input, maxlen=max_len)

        # Predict using the model
        prediction = model.predict(padded_input)

        # Determine sentiment based on the model's output
        sentiment = "Positive" if prediction[0] > 0.5 else "Negative"
        
        # Set the color depending on sentiment
        if sentiment == "Positive":
            sentiment_color = "color:green; font-size:24px;"
            confidence_color = "color:green; font-size:20px;"
        else:
            sentiment_color = "color:red; font-size:24px;"
            confidence_color = "color:red; font-size:20px;"
        
        # Display the sentiment in fancy style using markdown
        st.markdown(f"<p style='{sentiment_color}'>**Predicted Sentiment:** {sentiment}</p>", unsafe_allow_html=True)
    else:
        st.error("Please enter some text.")