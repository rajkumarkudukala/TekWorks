def sec_largest():
    max_1 , max_2 = list[0], list[1]
    for i in list:
        if i > max_1:
            max_2 = max_1
            max_1 = i
        elif i > max_2 and i < max_1:
            max_2 = i
    print(max_2)

list = [10,-4, 5, -7, -9, 1, 7, -6, 3]
sec_largest()
print(max(list))