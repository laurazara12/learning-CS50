def plate_try(plate):
    if is_valid(plate):
        return "Valid"
    else:
        return "Invalid"


def is_valid(s):
    half = len(s)//2
    if s.isalnum()and 2<=len(s) and len(s)<=6:
            if s[0:half].isalpha():
                if s[-2] != "0":
                    return True
    else:
        return False

if __name__ == "__main__":
    plate = input("Plate: ")
    print(plate_try(plate))