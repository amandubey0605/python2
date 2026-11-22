
import random

# -----------------------------------
# KANI V5.0 - CONVERSATION MEMORY
# -----------------------------------

responses = {
    "hello": [
        "Hey! How can I help you?",
        "Hello there! Nice to see you.",
        "Hey buddy! What's up?"
    ],
    "hi": [
        "Hello! Nice to meet you.",
        "Hi there!",
        "Hey! How are you?"
    ],
    "hey": [
        "Hey there!",
        "What's up?",
        "Hello buddy!"
    ],
    "how are you": [
        "I am doing great! What about you?",
        "I'm fine. Thanks for asking!",
        "Doing awesome! How about you?"
    ],
    "what is your name": [
        "My name is KANI, your reply bot.",
        "I'm KANI!",
        "You can call me KANI."
    ],
    "who created you": [
        "I was created by Aman using Python.",
        "Aman is my creator!",
        "I was built by Aman."
    ],
    "thank you": [
        "You're always welcome!",
        "Happy to help!",
        "My pleasure!"
    ],
    "thanks": [
        "You're welcome!",
        "Anytime!",
        "Glad I could help!"
    ],
    "good morning": [
        "Good morning! Have a wonderful day.",
        "A fresh day, a fresh start!",
        "Good morning! Stay positive."
    ],
    "good night": [
        "Good night! Sweet dreams.",
        "Sleep well!",
        "Have a peaceful night!"
    ]
}


# KANI's temporary memory
user_memory = {}


def show_welcome():
    print("=" * 45)
    print("             KANI - REPLY BOT")
    print("                 VERSION 5.0")
    print("=" * 45)
    print("KANI: Hello! I am KANI.")
    print("KANI: I can now remember your name.")
    print("KANI: Type 'help' to see commands.")
    print("KANI: Type 'bye' to exit.")
    print("=" * 45)


def get_reply(message):

    # 1. Remember user's name
    if message.startswith("my name is "):
        name = message.replace("my name is ", "", 1).strip().title()

        if name:
            user_memory["name"] = name
            return f"Nice to meet you, {name}!"

        return "Please tell me your name."

    # 2. Remember user's preferred name
    if message.startswith("call me "):
        name = message.replace("call me ", "", 1).strip().title()

        if name:
            user_memory["name"] = name
            return f"Sure! I'll call you {name}."

        return "What should I call you?"

    # 3. Recall user's name
    if "what is my name" in message or "what's my name" in message:

        if "name" in user_memory:
            return f"Your name is {user_memory['name']}."

        return "You haven't told me your name yet."

    # 4. Forget user's name
    if message == "forget my name":
        user_memory.pop("name", None)
        return "Okay! I have forgotten your name for this session."

    # 5. Help command
    if message == "help":
        return (
            "Available commands:\n"
            "- hello\n"
            "- hi\n"
            "- how are you\n"
            "- my name is Aman\n"
            "- what is my name\n"
            "- call me Aman\n"
            "- forget my name\n"
            "- bye"
        )

    # 6. Find a matching response
    for keyword, replies in responses.items():
        if keyword in message:
            return random.choice(replies)

    # 7. Default response
    return "Sorry, I don't understand that message yet."


def run_kani():

    show_welcome()

    while True:

        message = input("\nYou: ").strip().lower()

        # Exit commands
        if message in ["bye", "exit", "quit"]:
            print("KANI: Goodbye! Have a great day.")
            print("KANI: Shutting down...")
            break

        reply = get_reply(message)

        print("KANI:", reply)


if __name__ == "__main__":
    run_kani()
