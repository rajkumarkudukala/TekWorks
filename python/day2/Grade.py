def grade(m):
    if(m>100 or m<0):
        print("invalid marks")
    elif(m>80):
        print("Distinction")
    elif(m>70):
        print("A")
    elif(m>60):
        print("B")
    elif(m>50):
        print("C")
    elif(m>=40):
        print("D")
    else:
        print("Fail")
grade(int(input("Enter marks: ")))