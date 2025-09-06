def isStrong(n):
    for i in range(1,n+1):
        sum = 0
        n1 = i
        while n1>0:
            sum+=factorial(n1%10)
            n1//=10
        if(i == sum):
            print(i)
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact
isStrong(1000)