import streamlit as st
import random

# Initialize session state variables
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# Title
st.title("Number Guessing Game 🎲")

# Instructions
st.write("I'm thinking of a number between 1 and 100. Try to guess it!")

# User input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
submit = st.button("Guess")

if submit:
    st.session_state.attempts += 1
    if guess < st.session_state.random_number:
        st.write("🔼 Too low! Try a higher number.")
    elif guess > st.session_state.random_number:
        st.write("🔽 Too high! Try a lower number.")
    else:
        st.success(f"🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
        st.balloons()
        # Reset game
        st.session_state.random_number = random.randint(1, 100)
        st.session_state.attempts = 0

# Reset button
if st.button("Restart Game"):
    st.session_state.random_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.write("Game has been reset. Try guessing the new number!")