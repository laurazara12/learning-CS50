my_list = []
counts = {}
while True:
    try:
        item = input("")
        if item:
            item = item.upper()
            if item in counts:
                counts[item]+=1
            else:
                counts[item]=1
                my_list.append(item)
    except EOFError:
        my_list.sort()
        for item in my_list:
             print(counts[item], item)
        break