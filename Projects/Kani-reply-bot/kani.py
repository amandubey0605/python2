
print("=" * 40)
print("       KANI - REPLY BOT")
print("=" * 40)

print("\nKANI: Hello! I am KANI.")
print("KANI: I am ready to chat with you.")
print("KANI: Type 'bye' to exit.\n")

while True:

    message = input("You: ").strip().lower()

    if message == "hello" or message == "hi":
        print("KANI: Hey! How can I help you?")

    elif message == "how are you":
        print("KANI: I am doing great! What about you?")

    elif message == "what is your name":
        print("KANI: My name is KANI, your reply bot.")

    elif message == "who created you":
        print("KANI: I was created by Aman using Python.")

    elif message == "thank you" or message == "thanks":
        print("KANI: You're always welcome!")

    elif message == "bye":
        print("KANI: Goodbye! Have a great day.")
        print("KANI: Shutting down...")
        break

    else:
        print("KANI: Sorry, I don't understand that message yet.")

print("\nKANI: Session ended.")
