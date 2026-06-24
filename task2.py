print("1. Welcome to the Even or Odd Number Checker!")
number = int(input("Enter a number: "))

if number % 2 == 0:
 print("It's an Even Number.")
elif number % 2 != 0:
 print("It's an Odd Number.")

print("2. Positive, Negative or zero Checker! ")
number = int(input("Enter an integer: "))
if number > 0:
 print("The number is Positive. ")
elif number < 0:
 print("The number is Negative. ")
else:
 print("The number is Zero. ")

print("3. Age Category Checker! ")
age = int(input("Enter your age: "))
if age <= 10:
 print("CATEGORY: Child! ")
elif age <= 18:
 print("CATEGORY: Teenager! ")
elif age <= 35:
 print("CATEGORY: Adult! ")
else:
    print("CATEGORY: Senior! ")

print("4.Grade Calculator! ")
score = int(input("Enter your score (0-100): "))
if score >= 90:
 print("Grade: A")
elif score >= 80:
 print("Grade: B")
elif score >= 70:
 print("Grade: C")
elif score >= 60:
 print("Grade: D")
else:
 print("Grade: F")

print("5. vowel and consonant Checker! ")
a = input("Enter a letter: ")
if a == "a" or a == "A":
    print("The letter is a vowel.")
elif a == "e" or a == "E":
    print("The letter is a vowel.")
elif a == "i" or a == "I":
    print("The letter is a vowel.")
elif a == "o"or a == "O":
    print("The letter is a vowel.")
elif a == "u" or a == "U":
    print("The letter is a vowel.")
else:
    print("The letter is a consonant.")

print("6. Simple login system! ")
correct_username = "admin"
correct_password = "1234"
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid username or password. Please try again.")

print("7. Number comparison! ")
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))
if first_number > second_number and first_number > third_number:
 print("The first number is the largest.")
elif second_number > first_number and second_number > third_number:
 print("The second number is the largest.")
elif third_number > first_number and third_number > second_number:
 print("The third number is the largest.")

print("8. Days in a month! ")
month = input("Enter the month (1-12): ")
if month == "1" or month == "3" or month == "5" or month == "7" or month == "8" or month == "10" or month == "12":
 print("The month has 31 days.")
elif month == "4" or month == "6" or month == "9" or month == "11":
 print("The month has 30 days.")
elif month == "2":
 print("The month has 28 or 29 days (February).")

print("9. check if number is divided by 3 or 5! ")
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
 print("The number is divisible by both 3 and 5.")
elif number % 3 == 0:
 print("The number is divisible by 3.")
elif number % 5 == 0:
 print("The number is divisible by 5.")
else:
 print("The number is not divisible by 3 or 5.")
