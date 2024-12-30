# chatbot_nlp.py
import streamlit as st
from nltk.chat.util import Chat, reflections

# Define chatbot patterns and responses
pairs = [
    # Greetings
    [r"hi|hello|hey", ["Hello! How can I assist you today?", "Hi there! What can I help you with?"]],
    [r"good morning|good afternoon|good evening", ["Good day! How can I help you today?"]],

    # Personal Information
    [r"what is your name?", ["I am HelperBot, your virtual assistant.", "You can call me HelperBot."]],
    [r"who created you?", ["I was created by an enthusiastic programmer to assist you with your queries."]],
    
    # How are you?
    [r"how are you?", ["I'm just a program, but I'm here to help you! How about you?"]],
    [r"I am (.*)", ["It's great to hear that you are %1!", "Why do you feel %1?"]],

    # Help and Assistance
    [r"can you help me with (.*)", ["Sure, I can help you with %1. Could you provide more details?", "I'm here to assist! Let's dive into %1."]],
    [r"what can you do?", ["I can answer your questions, help you with tasks, and keep you engaged!"]],

    # Learning and Education
    [r"what is (.*)", ["%1 is a topic worth exploring. What would you like to know about it?", "I believe %1 has a lot to offer. Let's discuss!"]],
    [r"explain (.*)", ["Sure! Here's what I know about %1.", "Let me give you a brief about %1."]],

    # Favorites
    [r"what is your favorite (.*)", ["I don't have personal preferences, but I love helping people with %1."]],
    [r"do you like (.*)", ["I don't have emotions, but %1 seems interesting!"]],

    # Small Talk
    [r"tell me a joke", ["Why don’t scientists trust atoms? Because they make up everything!", "What do you get when you cross a snowman with a vampire? Frostbite!"]],
    [r"what is the weather like?", ["I'm not sure, but you can check an app for the latest updates."]],

    # Goodbye
    [r"bye|quit|exit", ["Goodbye! Have a wonderful day!", "Take care! See you next time."]],

    # Default Response
    [r"(.*)", ["I'm sorry, I don't understand that. Could you rephrase?", "Hmm, I don't know much about that. Let's try a different topic!"]]
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

# Streamlit UI for chatbot
st.title("Chatbot Using NLP")
st.markdown("### A friendly chatbot built using NLP.")

# User input
user_input = st.text_input("You:", placeholder="Type your message here...")

# Chatbot response
if user_input:
    response = chatbot.respond(user_input)
    if response:
        st.write(f"Chatbot: {response}")
    else:
        st.write("Chatbot: I'm sorry, I didn't understand that. Could you rephrase?")

