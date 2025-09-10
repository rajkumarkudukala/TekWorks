def freq(str):
    a = 0
    d = 0
    s = 0
    for i in str:
        if i.isalpha(): a+=1
        elif i.isdigit(): d+=1
        else: s+=1
    print("Alphabets:",a)
    print("Digits:",d)
    print("Special characters:",s)

freq("Hello@123, cvr@123&%$")