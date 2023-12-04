def shorten(word):
    try:
        word = str(word)
        vowels = "aeiouAEIOU"
        final_word = ""
        for char in word:
            if char not in vowels:
                final_word += char
        return f"{final_word}"
    except ValueError as e:
        print(e)
        sys.exit(1)

def main():
    print(f"Output: {shorten(word)}")

if __name__ == "__main__":
    word = input("Input: ")
    main()
