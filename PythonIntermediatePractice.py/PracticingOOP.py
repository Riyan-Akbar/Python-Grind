class Student:
    def __init__ (self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")

class Robot:
    def __init__(self,name,color,weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduceSelf(self):
        print(f"Hello my name is {self.name}. I am a {self.color} robot and i weight: {self.weight} kilograms")

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(self.balance)

    def withdraw(self,amount):
        self.balance = self.balance - amount
        if self.balance <= 0:
            print("No Balance")
        else:
            print(self.balance)

class Counter:
    def __init__(self,count=0):
        self.count = count
    def increment(self):
        self.count += 1
    def decrement(self):
        self.count -= 1
    def show(self):
        print(self.count)

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
        
    def perimeter(self):
        return 2*(self.length + self.width)

class Car:
    def __init__(self,brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed
    def accelerate(self,amount):
        self.speed = self.speed + amount
        return self.speed
    def brake(self,amount):
        self.speed = self.speed - amount
        if self.speed <= 0:
            self.speed = 0
            return self.speed
        else:
            return self.speed
    def show_speed(self):
        return self.speed

class ShoppingCart:
    def __init__(self):
        self.lst = []

    def add_item(self,item):
        self.lst.append(item)

    def remove_item(self,item):
        for i in range(len(self.lst)):
            if item in self.lst:
                self.lst.remove(item)
    
    def show_items(self):
        return self.lst

cart = ShoppingCart()

cart.add_item("Apple")
cart.add_item("Banana")
cart.add_item("Milk")

print(cart.show_items())

cart.remove_item("Banana")

print(cart.show_items())















# car = Car("Toyota", "Corolla")

# car.accelerate(50)
# car.accelerate(30)

# print(car.show_speed())

# car.brake(20)

# print(car.show_speed())

# car.brake(100)

# print(car.show_speed())

# r = Rectangle(10, 5)

# print(r.area())
# print(r.perimeter())

# c1 = Counter()
# c2 = Counter()

# c1.increment()
# c1.increment()

# c2.increment()

# c1.show()
# c2.show()

# RiyanAccount = BankAccount("Riyan",100000)
# RiyanAccount.deposit(10000)
# RiyanAccount.withdraw(20000)

# r1 = Robot("Tom","red",30)
# r2 = Robot("Jerry","blue",40)
# r1.introduceSelf()
# r2.introduceSelf()


# student1 = Student("Riyan",21,100)
# student1.display()