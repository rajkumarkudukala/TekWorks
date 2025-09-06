def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def rem(a,b):
    return a%b
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print("Addition of",a,b,":",add(a,b))
print("Subtraction of",a,b,":",sub(a,b))
print("Multiplication of",a,b,":",mul(a,b))
print("Division of",a,b,":",div(a,b))
print("Remainder when",a,"is divided by",b,":",rem(a,b))