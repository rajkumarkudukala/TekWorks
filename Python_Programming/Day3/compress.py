def compress(str):
    freq = {}
    for i in str:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for i in freq:
        print(i,freq[i],sep = '', end = '')

compress("aaabbca")