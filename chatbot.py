import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    ["hi|hello|hey", ["Hello!", "Hey there!", "Hi!"]],
    ["how are you?", ["I'm good, thank you!", "I'm doing well, thanks for asking."]],
    ["what's your name?", ["You can call me Chatbot.", "I'm just a chatbot."]],
    ["what can you do?", ["I can respond to basic questions and have simple conversations."]],
    ["quit", ["Bye, take care!", "Goodbye!"]],
]

# Create a Chat instance
chatbot = Chat(pairs, reflections)

# Define a function to chat with the user
def chat():
    print("Welcome! Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ").lower()
        response = chatbot.respond(user_input)
        if response:
            print("Chatbot:", response)
        else:
            print("Chatbot: Mhm I don't know that yet")
        if user_input == 'quit':
            break

# Run the chat function
if __name__ == "__main__":
    chat()
