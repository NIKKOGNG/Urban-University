my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = len(my_list)
i = 0
while i < a:
    if my_list[i] == 0:
        i += 1
    elif my_list[i] > 0:
        print(my_list[i])
        i += 1
    else:
        break