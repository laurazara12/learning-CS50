import emoji

def emojize_text(text):
    return emoji.emojize(text, language='alias' )

def main():
    user_input = input("Input: ").strip()
    emojized_input = emojize_text(user_input )
    print(emojized_input)

if __name__ == "__main__":
    main()
