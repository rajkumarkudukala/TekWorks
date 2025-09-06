def isEven(n):
    return n%2 == 0
n = int(input("Enter a number: "))
if(isEven(n)):
    print("Even")
else:
    print("Odd")