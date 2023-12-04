def convert(text):
    text = text.replace(':)', '🙂')
    text = text.replace(':(', '🙁')
    return text

def main():
    user_input = input("Please enter text with emoticons (e.g., :), :(): ")
    result = convert(user_input)
    print("Converted text:", result)

if __name__ == "__main__":
    main()
