import inflect

my_list = []

# Loop to input names until EOF (Control-D)
while True:
    try:
        user_input = input("Input: ")
        my_list.append(user_input)
    except EOFError:
        break

s = ""
if len(my_list) > 0:
    s = "Adieu, adieu, to "
    if len(my_list) == 1:
        s += my_list[0]
    elif len(my_list) == 2:
        s += " and ".join(my_list)
    else:
        s += ", ".join(my_list[:-1]) + ", and " + my_list[-1]

print(s)
