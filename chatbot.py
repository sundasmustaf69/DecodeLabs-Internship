# =========================================
# DecodeLabs Project 1
# Rule-Based AI Chatbot

print("=" * 50)
print("🤖 Welcome to the AI Rule-Based Chatbot")
print("Type 'help' to see available commands")
print("Type 'bye' to exit the chatbot")
print("=" * 50)

while True:

    user = input("\nYou: ").lower().strip()

    # Greetings
    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! Nice to meet you 😊")

    elif user == "assalam o alaikum":
        print("Bot: Walikum Assalam 🌸")

    # Basic conversation
    elif user == "how are you":
        print("Bot: I'm doing great! Thanks for asking 😄")

    elif user == "your name":
        print("Bot: I am DecodeLabs AI Chatbot 🤖")

    elif user == "who made you":
        print("Bot: I was created as Project 1 for DecodeLabs Internship 🚀")

    elif user == "what can you do":
        print("Bot: I can chat with you using rule-based logic.")

    # Time-based response
    elif user == "good morning":
        print("Bot: Good Morning! Have a productive day ☀️")

    elif user == "good night":
        print("Bot: Good Night! Sleep well 🌙")

    # Fun responses
    elif user == "tell me a joke":
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs 😂")

    elif user == "motivate me":
        print("Bot: Success starts with consistency. Keep learning 🚀")

    # Help command
    elif user == "help":
        print("\nAvailable Commands:")
        print("- hello / hi")
        print("- how are you")
        print("- your name")
        print("- who made you")
        print("- what can you do")
        print("- good morning")
        print("- good night")
        print("- tell me a joke")
        print("- motivate me")
        print("- bye")

    # Exit condition
    elif user == "bye":
        print("Bot: Goodbye! Thanks for chatting 😊")
        break

    # Empty input
    elif user == "":
        print("Bot: Please type something.")

    # Unknown command
    else:
        print("Bot: Sorry, I don't understand that command.")