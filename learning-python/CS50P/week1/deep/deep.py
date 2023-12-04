def main():
    user_input = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").strip()

    user_input_lower = user_input.lower()
    if user_input_lower == '42' or 'forty-two' in user_input_lower or 'forty two' in user_input_lower:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
