def length(str):
    count = 0
    for i in str:
        count+=1
    return count

print(length("Hello"))

def compare(str1, str2):
    return str1 == str2

s1 = "aa"
s2 = "aa"
print(s1,"==",s2,":",compare(s1,s2))

def concat(str1, str2):
    return str1+str2

print(concat("Hello","World"))