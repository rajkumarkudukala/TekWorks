def min_max_freq(str):
    freq = {}
    for i in str:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    max = str[0]
    min = str[0]
    for i in freq:
        if freq[i] > freq[max]:
            max = i
        if freq[i] < freq[min]:
            min = i
    print("Highest frequency character:",max,freq[max])
    print("Lowest frequency character:",min,freq[min])

min_max_freq("aaabbbbbaaaabbbbjhdsxnbsggggg")