class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll_no = roll
        self.marks = marks

    def display(self):
        print(self.name)
        print(self.roll_no)
        print(self.marks)

st1 = Student("Raj", "G1", 100)
st2 = Student("Dhamodar", "D7", 100)

st1.display()
st2.display()