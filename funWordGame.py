import streamlit as st
import random

# List of words for the game
words = ["apple", "banana", "cherry", "orange", "grape", "mango", "lemon", "kiwi"]

# Select a random word
random_word = random.choice(words)
reversed_word = random_word[::-1]  

# Custom CSS for styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #e68; 
            padding: 20px;
        }

        /* Input box design */
        div[data-baseweb="input"] {
            background-color: #2d2d2d; /* Dark Grey */
            color: white;
            box-shadow: 5px 5px 12px rgba(0, 0, 0, 0.3);
            border-radius: 8px;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("🎮 Fun Word Guessing Game")

# Instructions
st.write("🔹 Aapko ek **random word** diya jayega.") 
st.write("🔹 Aapko us word ka **reverse likhna** hoga.")
st.write("🔹 Example: `apple` → `elppa`")

# Show the word
st.subheader(f"👉 Your Word: **{random_word}**")

# User input
user_guess = st.text_input("Type the reversed word:")

# Check Button
if st.button("Check Answer"):
    if user_guess.lower() == reversed_word:
        st.success("🎉 Correct! Well done! 🚀")
    else:
        st.error(f"❌ Incorrect! The correct answer was: **{reversed_word}**")

