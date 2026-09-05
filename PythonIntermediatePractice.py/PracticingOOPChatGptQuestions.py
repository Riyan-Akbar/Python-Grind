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

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1
        return self.age 
    def show_info(self):
        return (f"Name: {self.name}, Age: {self.age}")

class Student:

    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
        # marks = [] not required as the data type is already understood by py when we pass them in the functions

    def average(self):
        return sum(self.marks)/ len(self.marks)
    def highest_mark(self):
        return max(self.marks)

class Book:
    def __init__(self,title,author,avaible = True):
        self.title = title
        self.author = author
        self.avaible = avaible


    def borrow(self):
        if self.avaible == True:
            self.avaible = False
            return ("Book borrowed")
        else:
            return ("Book is not avaible")

    def return_book(self):
        if self.avaible == False:
            self.avaible = True
            return ("Book returned")
        else:
            return ("Book was not borrowed")

class BankAccount:
    # def __init__(self,owner,balance = 0,transactions = []): this is because if i put [] in there it will become a global variable shared between any two objects , so dont do that . when asked to create a list do it inside the init constructor for variables for each obj separately.
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance
        self.transactions = [] 

    def deposit(self,amount):
        self.balance = self.balance + amount
        self.transactions.append(amount)

    def withdraw(self,amount):
        # if self.balance - amount <= 0: this is wrong , as if a person had 10 and we run it throug this if st we will get false.
        if amount > self.balance:
            return False
        else:
            self.balance = self.balance - amount
            self.transactions.append(-amount)
            return True

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions





    













# account = BankAccount("Riyan", 1000)

# account.deposit(500)
# account.withdraw(200)
# account.withdraw(2000)

# print(account.get_balance())
# print(account.get_transactions())

# book = Book("Harry Potter", "J.K. Rowling")

# print(book.borrow())
# print(book.borrow())

# print(book.return_book())
# print(book.return_book())


# student = Student("Riyan", [80, 90, 75, 95])

# print(student.average())
# print(student.highest_mark())

# dog1 = Dog("Bruno", 3)
# dog2 = Dog("Max", 5)

# dog1.birthday()
# dog1.birthday()

# dog2.birthday()

# print(dog1.show_info())
# print(dog2.show_info())

# cart = ShoppingCart()

# cart.add_item("Apple")
# cart.add_item("Banana")
# cart.add_item("Milk")

# print(cart.show_items())

# cart.remove_item("Banana")

# print(cart.show_items())

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

# Andy = Microwave()
# print(Andy)

# student1 = Student("Riyan",21,100)
# student1.display()