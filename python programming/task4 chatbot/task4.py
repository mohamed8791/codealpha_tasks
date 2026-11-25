def get_response(user_input):
    message=user_input.lower().strip()
    if message in  ("hello","hi","hey"):
        return "Hi!,How are you?"
    elif message in ("how are you?","how are you"):
        return "I am fine, thanks"
    elif message in ("bye","goodbye"):
        return "Goodbye!"
    else:
     return "Sorry, I don't understand that. Try saying hello, how are you, or bye."

def main():
    while True:
        user_input = input("\nYou:")
        response = get_response(user_input)
        print(f"Bot:{response}")
        if user_input.lower().strip() in ("bye","goodbye","see you"):
            break

if __name__ == "__main__":
    main()