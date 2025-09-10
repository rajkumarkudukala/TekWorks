def unique(list):
    freq = {}
    for i in list:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for i in freq:
        if freq[i] == 1:
            print(i)

unique([1,1,2,2,2,2,3,4,5,9,8,4,4,2,2,6,56,18])