# class SocialMedia:

#     CEO = "Mark"

#     def like(self):
#         print("Liked")

#     def comment(self):
#         print("Commented")

#     def post(self):
#             print("Posted")

# facebook = SocialMedia()
# facebook.comment()
# facebook.post()
# facebook.like()


# class car:

#     color = "Black"
#     brand = "Rolls Royce"
#     milage = "3mph"

#     def engin(self):
#         print("RR Engine")

#     def drive(self):
#         print("Driving")

#     def honk(self):
#         print("Peeeeeeeeeeeeeeeeee")

# a = car()
# b = car()

# print(a.brand)
# print(b.brand)

# b.brand = "Honda"
# b.milage = "25mph"

# print(a.brand)
# print(b.brand)

# class Dog:

#     species = "GS"

#     def eat(self):
#         self.b = 50
#         print(f"hungry right now.")

#     def bark(self):
#         print(self.b)
#         print(f"says woof!")

# a = Dog()
# a.eat()
# a.bark()

# class employee:
#  def adddata(self):
#   self.id=int(input("Enter Employee ID:"))
#   self.name=input("Enter Employee Name:")
#   self.mob=int(input("Enter Mobile Number:"))
#   self.salary=int(input("Enter Employee Salary:"))

#  def display(self):
#      print("Employee ID;" , self.id)
#      print("Employee Name;" , self.name)
#      print("Employee Mob no;" , self.mob)
#      print("Employee Salary;" , self.salary)

# a=employee()
# a.adddata()
# a.display()


#Create a Circle class with the attribute radius. Write methods to calculate the area and circumference (perimeter) of the circle.
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14159 * (self.radius ** 2)

#     def circumference(self):
#         return 2 * 3.14 * self.radius

# r = float(input("Enter radius: "))

# c = Circle(r)

# print(f"Area: {c.area():}")
# print(f"Circumference: {c.circumference():}")

# #Create a Rectangle class using a constructor to initialize length and width. Write methods to display the dimensions and calculate the area.
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# l = float(input("Enter length: "))
# w = float(input("Enter width: "))

# rect = Rectangle(l, w)

# print(f"Dimensions: {rect.length} x {rect.width}")
# print(f"Area: {rect.area()}")

#Create a Student class. Accept student information using a constructor and write a method to calculate the total marks.
# class Student:
#     def __init__(self, name, roll_no, marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks  

#     def total_marks(self):
#         return sum(self.marks)


# name = input("Enter student name: ")
# roll = input("Enter roll number: ")

# marks_input = input("Enter marks separated by space: ")
# marks_list = [float(m) for m in marks_input.split()]

# student = Student(name, roll, marks_list)
# print("\n--- Student Info ---")
# print(f"Name: {student.name}")
# print(f"Roll No: {student.roll_no}")
# print(f"Total Marks: {student.total_marks()}")

#Create a Mobile class using a constructor to initialize the brand, RAM, and storage. Write a method to print all specifications.
class Mobile:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

    def display_specs(self):
        print("\n--- Mobile Specifications ---")
        print(f"Brand:   {self.brand}")
        print(f"RAM:     {self.ram} GB")
        print(f"Storage: {self.storage} GB")

brand = input("Enter mobile brand: ")
ram = input("Enter RAM (in GB): ")
storage = input("Enter Storage (in GB): ")

my_phone = Mobile(brand, ram, storage)

my_phone.display_specs()




