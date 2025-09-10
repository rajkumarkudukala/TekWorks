def occurance_count(str,ch):
    count = 0
    for i in str:
        if i == ch:
            count+=1
    return count

c = occurance_count("Raj Kumar","a")
print(c)