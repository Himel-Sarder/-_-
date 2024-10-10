import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"(hi|hello|hey|heya|howdy)",
        ["Hello there! How can I assist you today?", "Hi! How are you doing today?"]
    ],
    [
        r"what is your name ?",
        ["I'm a chatbot created by Himel Sarder. What's your name?"]
    ],
    [
        r"my name is (.*)",
        ["Lovely to meet you, %1! How can I be of service today?", "Hello %1! How can I assist you?"]
    ],
    [
        r"how are you ?",
        ["I'm just a bunch of code, so I don’t have feelings, but I’m ready to help! How are you?"]
    ],
    [
        r"what can you do ?",
        ["I'm here to chat, answer your questions, and assist with basic tasks. What would you like help with?"]
    ],
    [
        r"(.*) created you ?",
        ["I was created by Himel Sarder, a passionate programmer!"]
    ],
    [
        r"(.*)(help|support)(.*)",
        ["I'm here to support you! What do you need assistance with?", "How can I help you today?"]
    ],
    [
        r"i feel (.*)",
        ["I'm sorry you feel %1. Sometimes talking about it helps. Do you want to share more?"]
    ],
    [
        r"tell me a joke",
        ["Why don't programmers like nature? It has too many bugs! 😂", "I only know programming jokes! Here’s one: Why do programmers prefer dark mode? Because light attracts bugs! 😄"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! It was nice chatting with you. Have a wonderful day!", "See you soon! Take care!"]
    ],
    [
        r"(.*)",
        ["I'm not quite sure what you mean. Can you rephrase that?", "Sorry, I didn’t catch that. Could you say it in a different way?"]
    ]
]

# Reflections dictionary to adjust responses dynamically
reflections = {
    "i am": "you are",
    "i'm": "you are",
    "are": "am",
    "you're": "I am",
    "your": "my",
    "you": "me",
    "me": "you"
}

# Initialize the chatbot with pairs and reflections
chatbot = Chat(pairs, reflections)

# Function to start conversation
def chatbot_conversation():
    print("🤖 Hi! I'm your personal chatbot created by Himel Sarder. Type 'bye' to end the conversation anytime. 😊")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("Chatbot: 👋 Goodbye! Have a great day ahead!")
            break
        else:
            print(f"Chatbot: {chatbot.respond(user_input)}")

# Start the conversation
if __name__ == "__main__":
    chatbot_conversation()
