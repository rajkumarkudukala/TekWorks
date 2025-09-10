def topper(students):
    topper = students[0]
    for i in students:
        if i[2] > topper[2]:
            topper = i
    return topper[1]

def above75(students):
    list = []
    for i in students:
        if i[2] > 75:
            list.append(i)
    for i in list:
        print(i[1])

students = [(101, 'aaa', 89), (102, 'bbb', 74), (103, 'ccc', 83), (104, 'ddd', 90), (105, 'eee', 64)]
print("Topper:",topper(students))
print("Students who scored Above 75: ")
above75(students)