
def main(a,b):
    try:
        a = int(a)
        b = int(b)
        return a * b
    except ValueError:
        print("The values inputed were not both integers")

if __name__ == "__main__":
    a = input("a: ")
    b = input("b: ")
    print ("result: ",main(a,b))