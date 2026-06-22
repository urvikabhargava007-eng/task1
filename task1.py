# 1) Ask the user for their age
print(" Q1: Ask the user's age and print True if they can vote (18 or older), otherwise False")
age = int(input("Please enter your age: "))

# Check if they are eligible to vote (18 or older)
eligible_to_vote = age >= 18
print(eligible_to_vote)

# 2) Ask the user for their marks
print("Q2: Ask for marks and print True if marks are 40 or above.")
marks = float(input("Enter your marks: "))

# Check if marks are 40 or above
is_pass = marks >= 40
print(is_pass)

# 3) Ask the user for a number
print("Q3: Print True if a number is even.")
number = int(input("Enter a number: "))

# Check if the number is even
# (A number is even if the remainder when divided by 2 is exactly 0)
is_even = (number % 2) == 0
print(is_even)

# 4) Ask the user for a number
print("Q4: Negative Number Check")
number = float(input("Enter a number: "))

# Check if the number is negative (less than 0)
is_negative = number < 0
print(is_negative)

# 5) Ask the user for two numbers
print("Q5: Ask for two numbers and print True if they are equal.")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check if the two numbers are equal
are_equal = num1 == num2
print(are_equal)

# 6) Ask the user for two numbers
print("Q6: Print True if the first number is greater than the second.")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check if the first number is greater than the second
is_greater = num1 > num2
print(is_greater)

# 7) Ask the user for a number
print("Q7: Q: Print True if a number is divisible by 5")
number = int(input("Enter a number: "))

# Check if the number is divisible by 5
# (A number is divisible by 5 if the remainder is 0)
is_divisible_by_5 = (number % 5) == 0
print(is_divisible_by_5)


# 8) Ask the user for a number
print("Q8: Ask a number and print its square.")
number = float(input("Enter a number: "))

# Calculate the square (multiply the number by itself)
square = number ** 2

# Print the result
print("The square of the number is:", square)

# 9) Ask the user for a number
print("Q9: Print True if the square of a number is greater than 100.")
number = float(input("Enter a number: "))

# Check if the square of the number is greater than 100
is_greater_than_100 = (number ** 2) > 100
print(is_greater_than_100)


# 10) Ask the user for a number
print("Q10: Print True if a number leaves remainder 1 when divided by  3")
number = int(input("Enter a number: "))

# Check if the number leaves a remainder of 1 when divided by 3
leaves_remainder_1 = (number % 3) == 1
print(leaves_remainder_1)

# 11) Ask the user for marks in three subjects
print("Q11: Ask marks in 3 subjects and print True if the average is at least 50.")
sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))

# Calculate the average
average = (sub1 + sub2 + sub3) / 3

# Check if the average is at least 50
is_pass = average >= 50
print(is_pass)




