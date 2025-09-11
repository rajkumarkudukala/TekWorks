#TASK-1
class Vehicle:
    def __init__(self, owner, licence):
        self.__owner = owner
        self.__licence = licence
    def display(self):
        print(self.__owner)
        print(self.__licence)
    def get_owner(self):
        return self.__owner
    def get_licence(self):
        return self.__licence
    def calculate_parking_fee(self):
        return 0
    
class Bike(Vehicle):
    def __init__(self, owner, licence):
        super().__init__(owner, licence)
        self.helmet_required = True
    def calculate_parking_fee(self, hours):
        return 20*hours
    def display(self):
        super().display()
        print(self.calculate_parking_fee(1))
    
class Car(Vehicle):
    def __init__(self, owner, licence, seats):
        super().__init__(owner, licence)
        self.seats = seats

    def calculate_parking_fee(self, hours):
        return 50*hours
    
    def display(self):
        super().display()
        print(self.calculate_parking_fee(1))
    
class SUV(Vehicle):
    def __init__(self, owner, licence):
        super().__init__(owner, licence)
        self.four_wheel = True

    def calculate_parking_fee(self,hours):
        return 70*hours
    def display(self):
        super().display()
        print(self.calculate_parking_fee(1))
    
class Truck(Vehicle):
    def __init__(self, owner, licence):
        super().__init__(owner, licence)

    def calculate_parking_fee(self, hours):
        return 100*hours
    def display(self):
        super().display()
        print(self.calculate_parking_fee(1))

vehicles = [Bike("aaa",1111), Car("bbb",222,4), SUV("ccc",333), Truck("ddd",444)]
for i in vehicles:
    i.display()

#TASK-2
class Parking