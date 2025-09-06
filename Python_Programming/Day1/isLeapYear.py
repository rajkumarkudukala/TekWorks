def isLeapYear(n):
    if(n%4==0):
        if(n%100==0):
            if(n%400==0):
                print("Leap Year")
            else:
                print("Not a Leap Year")
        else:
            ("Leap Year")
    else:
        print("Not a Leap Year")

isLeapYear(2000)