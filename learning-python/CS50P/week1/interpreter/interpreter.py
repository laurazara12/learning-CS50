def main():
    expression = input("Enter an arithmetic expression (e.g., 1 + 1): ")
    x, operator, z = expression.split()

    x = float(x)
    z = float(z)

    if operator == '+':
        result = x + z
    elif operator == '-':
        result = x - z
    elif operator == '*':
        result = x * z
    elif operator == '/':
        result = x / z

    print(f"Result: {result:.1f}")

if __name__ == "__main__":
    main()
