# Simple Chatbot

def chatbot():
    print("Chatbot: Hi! How can I assist you today?")
    while True:
        user = input("You: ").lower().strip()

        if user in ('bye', 'exit', 'leave'):
            print("Chatbot: Goodbye!")
            break

        elif any(greet in user for greet in ('hello', 'hi', 'hey')):
            print("Chatbot: Hi! How can I help you today?")

        elif 'price' in user or 'cost' in user:
            print("Chatbot: Prices depend on the product. Which product do you require?")

        elif 'product' in user or 'products' in user:
            print("Chatbot: Here is a list of products you can buy: ")

        elif 'help' in user or 'issue' in user:
            print("Chatbot: Please describe your issue briefly.")

        else:
            print("Chatbot: Sorry, I couldn't understand you. Please rephrase.")

# Main
chatbot()
