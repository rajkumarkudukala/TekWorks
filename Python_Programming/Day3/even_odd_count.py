def even_count():
    e = 0
    o = 0
    for i in list:
        if i%2 == 0:
            e += 1
        else:
            o += 1
    print("Even:",e,"Odd:",o)
list = [1,-4, 5, -7, -9, 1, 7, -6, 3]
even_count()