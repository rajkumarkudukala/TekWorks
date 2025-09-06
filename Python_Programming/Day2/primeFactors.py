i = int(input("Enter a number: "))
for j in range(1,i+1):
    if(i%j==0):
        f = 0
        for k in range(1,j+1):
            if j%k == 0:
                f+=1
        if(f == 2):
            print(j)