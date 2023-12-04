from validator_collection import validators, errors

def response(value):
    try:
        validators.email(value)
        return "Valid"
    except ValueError:
        return "Invalid"

def main():
    result = response(str(input("Email: ")))
    print(result)

if __name__ == "__main__":
    main()
