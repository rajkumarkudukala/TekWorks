def primes(n):
    for i in range(1,n+1):
        f = 0
        for j in range(1,i+1):
            if i%j == 0:
                f+=1
        if(f==2):
            print(i)
primes(int(input("Enter a number: ")))





