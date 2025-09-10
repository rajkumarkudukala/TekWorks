def frequency(list):
    freq = {}
    for i in list:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    print(freq)

frequency([1,1,1,2,2,2,2,3,4,5,3,3,9,8,4,4,2,2])