class Student:
    def __init__ (self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")

student1 = Student("Riyan",21,100)
student1.display()