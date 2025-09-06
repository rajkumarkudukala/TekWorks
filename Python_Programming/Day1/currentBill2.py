def currentBill(n):
    if(n<=50):
        return n*3.80
    elif(n<=100):
        return (50*3.80)+(n-50)*4.20
    elif(n<=200):
        return (50*3.80)+(50*4.20)+(n-100)*5.10
    elif(n<=300):
        return (50*3.80)+50*4.20+100*5.10+(n-200)*6.30
    else:
        return (50*3.80)+50*4.20+100*5.10+100*6.30+(n-300)*7.50
print(currentBill(int(input("Enter no.of units: "))))