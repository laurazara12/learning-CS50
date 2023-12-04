import random

def guess(level):
    num = random.randint(0, level)
    while True:
        try:
            guess_num = int(input("Guess: "))
            if guess_num > num:
                print("Too large!")
            elif guess_num < num:
                print("Too small!")
            else:
                print ("Just right!")
                return num
        except ValueError:
            print("Not an int")

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            print(guess(level))
            break
    except ValueError:
        print("Not an int")
