def isArmstrong(n):
    for i in range(1,n+1):
        sum = 0
        n1 = i
        while n1>0:
            sum+=(n1%10)**3
            n1//=10
        if(i == sum):
            print(i)
isArmstrong(1000)