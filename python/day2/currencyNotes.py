def notes(n):
    l = [2000,500,200,100,50,20,10,5,2,1]
    c = 0
    for i in l:
        c += n//i
        if(n//i>0):
            print(i,":",n//i)
        n = n%i
    print("Total :",c)
notes(2560)