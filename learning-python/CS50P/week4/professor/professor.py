import random


def main():
    level  = get_level()
    score = 0

    for _ in range(10):
        a, b = generate_integer(level)
        result = a + b
        tries = 0

        while tries < 3:
            try:
                trial = int(input(f"{a} + {b} = "))
                if trial == result:
                    score+=1
                    break
                else:
                    print("EEE")
                    tries+=1
            except ValueError:
                print("EEE")

        if tries == 3:
            print(result)
    print(f"Your score is: {score}/10")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                 return level
            else:
                raise ValueError("EEE")
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")


def generate_integer(level):
    if level == 1:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
    elif level == 2:
        a = random.randint(10, 99)
        b = random.randint(10, 99)
    else:
        a = random.randint(100, 999)
        b = random.randint(100, 999)
    return a,b

if __name__ == "__main__":
    main()