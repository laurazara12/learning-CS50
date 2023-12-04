c = 0
print("Change Owed: 50 ")
while True:

    a = input("Insert coin: ").strip()
    if a.isdigit():
        a = int(a)
        if a in [25,10,5]:
            c += a
        if c < 50:
            amount_due = 50-c
            print(f"Amount Due: {amount_due }")
            continue
        else:
            change_owed = abs(50-c)
            print(f"Change Owed: {change_owed}")
            break
