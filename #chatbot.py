import time

# Get current time
now = time.ctime()

# Dictionary of questions and answers
qna = {
    "hi": "Hello!",
    "how are you": "I'm doing great, thank you!",
    "what is your name": "My name is Aarti.",
    "how old are you": "I am 20 years old.",
    "what is the time now": now,
    "surname": "Jatav",
    "apple color": "Red",
    "banana color": "Yellow",
    "alphabet letters": "26",
    "sky color": "Sky Blue"
}

# Welcome message
print("👋 Welcome to Aarti's Chatbot!")
print("Type 'quit' to exit the chat.\n")

# Chat loop
while True:
    qs = input("Ask me something: ").strip().lower()

    if qs == "quit":
        print("👋 Goodbye! Have a great day!")
        break

    # Respond if question is in dictionary
    if qs in qna:
        print("🤖", qna[qs])
    else:
        print("🤖 I don't understand that question.")