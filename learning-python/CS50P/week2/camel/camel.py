def main(camil_case):
    snake_case = ""
    for _ in camil_case:
        if _.isupper():
           snake_case += "_"
        snake_case += _.lower()
    return snake_case

a = input("Input")
b = main(a)
print(b)