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




 # 2

# Simple Medical Expert System
print("=== DOCTOR BOT ===")
print("I can help with common health issues")

# Ask about symptoms
print("\nWhat symptoms do you have?")
print("1. Fever and Cough")
print("2. Headache")
print("3. Stomach Pain")
print("4. Chest Pain")

choice = input("Choose 1-4: ")

# Give diagnosis based on choice
if choice == "1":
    print("\nPossible: Cold or Flu")
    print("Treatment: Rest, drink water, take medicine")
    print("See doctor if not better in 3 days")

elif choice == "2":
    print("\nPossible: Headache or Migraine")
    print("Treatment: Rest in dark room, pain relievers")
    print("See doctor if severe")

elif choice == "3":
    print("\nPossible: Indigestion or Food issue")
    print("Treatment: Light food, rest")
    print("See doctor if pain continues")

elif choice == "4":
    print("\n⚠️  WARNING: CHEST PAIN")
    print("Possible: Heart problem")
    print("Go to hospital immediately!")

else:
    print("Please choose 1-4")

print("\nRemember: I'm just a computer!")
print("Always see a real doctor! 🏥")
