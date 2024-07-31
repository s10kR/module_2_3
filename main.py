my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, -5]
number = 0
while number < len(my_list):
    new_list = my_list[number]
    number = number + 1
    if new_list == 0:
        continue
    elif new_list < 0:
        break
    else:
        print(new_list)
