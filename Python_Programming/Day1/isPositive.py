def isPositive(n):
    return n >= 0
n = int(input("Enter a number: "))
if(isPositive(n)):
    print("Positive")
else:
    print("Negative")