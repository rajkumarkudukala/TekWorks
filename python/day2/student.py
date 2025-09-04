sno = int(input("Enter Student number: "))
sname = input("Enter Student name: ")
marks = list(map(int, input("Enter marks: ").split()))
total = 0
for i in marks:
    total+=i
avg = total/3
round(avg, 2)
print("total: ",total)
print("Average: ", avg)