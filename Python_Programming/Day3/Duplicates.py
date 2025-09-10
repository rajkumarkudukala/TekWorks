def unique(list):
    l = []
    for i in list:
        if i not in l:
            l.append(i)
    print(l)
    print("Duplicate:",len(list) - len(l))

unique([1,1,1,2,2,2,2,3,4,5,3,3,9,8,4,4,2,2])