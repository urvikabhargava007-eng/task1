# def odd_even_check():
#     a = int(input("Enter a number:"))
#     if a % 2 == 0:
#             print("even")   
#     else:
#         print("odd")  
# odd_even_check()


# def div_checker_by_3():
#  a = int(input("Enter a number:"))
#  if a % 3 ==0:
#     print("Yes it is divisible by 3")
#  else:
#     print("No it is not divisible by 3")
# div_checker_by_3()

# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def div(a,b):
#     print(a/b)

# a = int(input("Enter a number:"))
# b = int(input("Enter b number:"))

# add(a,b)
# sub(a,b)
# mul(a,b)
# div(a,b)

# def odd_even_check(a,b,c,d,e):
# docstring
#  "this function lets you to check wheather the number is odd or even."
#  numbers = [a,b,c,d,e]
#  for num in numbers:
#      if num  % 2 == 0:
#             print("even")   
#      else:
#         print("odd")  
# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))
# c = int(input("Enter a number:"))
# d = int(input("Enter a number:"))
# e = int(input("Enter a number:"))
# odd_even_check(a,b,c,d,e)

# a = int(input("Enter 1st number:"))
# b = int(input("Enter 2nd number:"))
# numbers = [a,b]

# 1. Print Sum of Elements
# def print_sum_of_elements(numbers):
#   total_sum = sum(numbers)
    
#   print("sum of elements:" , total_sum)
# my_list = [10, 20, 30, 40, 50]
# print_sum_of_elements(my_list)

# 2. Print Largest Number
# def print_largest(numbers):
#     if numbers:
#         largest = max(numbers)
#         print("2. Largest:", largest)
# my_list = [10, 20, 30, 40, 50]
# print_largest(my_list)

# 3. Print Smallest Number
# def print_smallest(numbers):
#     if numbers:
#         smallest = min(numbers)
#         print("3. Smallest:", smallest)
# my_list = [10, 20, 30, 40, 50]
# print_smallest(my_list)

# 4. Search for an Element
#def search_element():





#5. Count Even Numbers
# def count_evens(numbers):
#     evens = sum(1 for x in numbers if x % 2 == 0)
#     print("5. Even count:", evens)
# my_list = [10, 20, 30, 40, 50]
# count_evens(my_list)

# 6. Count Odd Numbers
# def count_odds(numbers):
#     odds = sum(1 for x in numbers if x % 2 != 0)
#     print("6. Odd count:", odds)
# my_list = [10, 20, 30, 40, 50]
# count_odds(my_list)

# 7. Print Average
# def print_average(numbers):
#     if numbers:
#         avg = sum(numbers) / len(numbers)
#         print("7. Average:", avg)
# my_list = [10, 20, 30, 40, 50]
# print_average(my_list)

# 8. Count Positives and Negatives
#def count_positives_negatives(numbers):



   

# 9. Count Vowels
#def count_vowels(text):


    

# 10. Check Palindrome
#def check_palindrome(text):


    

# 11. Print Numbers Divisible by 5
# def div_checker_by_5():
#      a = int(input("Enter a number:"))
#      if a % 5 ==0:
#       print("Yes it is divisible by 5")
#      else:
#       print("No it is not divisible by 5")
# div_checker_by_5()

# 12. Print Common Elements
#def print_common_elements(list1, list2):


    
# 13. Print Factorial of Each Element
#def print_factorials(numbers):






# 14. Print Prime Numbers
# data = int(input("Enter a number:"))
# def prime_checker(data):
#     i = 2
#     while i < data:
#         if data % i == 0:
#             print("It is not a prime number")
#             break
#         i += 1
#     if i == data:
#         print("It is a prime number")

# prime_checker(data)





# def test(number1 , number2 , op="*"):
#     if op == "*":
#         return number1 * number2
#     elif op == "+":
#         return number1 + number2
#     elif op == "/":
#         return number1 / number2
#     elif op == "-":
#         return number1 - number2
    
# output = test(10,20, "%")
# print(output)


# def test():
#     while True:
#         return True
# print( test())

# def divide_checker(number):
#     for x in range(2, number):
#         if number % x == 0:
#             return True
#     return False
# print(divide_checker(3))



# data = int(input("Enter a number:"))
# def prime_checker(data):
#     i = 2
#     while i < data:
#         if data % i == 0:
#             return "It is not a prime number"
#         i += 1
#     return "It is a prime number"

# print(prime_checker(data))

#UPPER CHECKER
# data = input("Enter a string:")

# def upper_checker(data):
#     for i in data:
#         if i in "abcdefghijklmnopqrstuvwxyz":
#             return False
#     return True
# print(upper_checker(data))

#COUNT CHECKER
# def count(data , what_to_count):
#     counter = 0
#     for x in data:
#         if x == what_to_count:
#             counter += 1
#     return counter

# print(count("abcdabcdabfdcdfr" , "a"))

#EVEN FILTER
# def even_filter(data):

#     even = []
#     for x in data:
#         if x % 2 == 0:
#             even.append(x)
#     return even

# a = even_filter([10, 20, 30, 40, 67, 75, 93])
# print(a)

#SMALLEST DIVISOR

# def smallest_divisor(number):
#     for x in range(2, number):
#         if number % x == 0:
#             return x
#     return number

# print(smallest_divisor(7))

#Sum of Elements

#Using print: Write a function that takes a list of integers and prints the sum of all the elements.
# def print_sum(numbers):
#     total = sum(numbers)
#     print("Sum:", total)

# print_sum([10, 20, 30, 40])

# #Using return: Write a function that takes a list of integers and returns the sum of all the elements.
# def get_sum(numbers):
#     return sum(numbers)

# output = get_sum([10, 20, 30, 40])

# print("Returned Sum:", output)
# print("Double the Sum:", output * 2)

#Largest Number

#Using print: Write a function that takes a list of integers and prints the largest number in the list.
# data = input("Enter integers separated by space: ")
# number_list = [int(x) for x in data.split()]
# def print_largest(data):
#     if not data:
#         print("The list is empty!")
#         return

#     # Start by assuming the first number is the largest
#     largest = data[0]

#     # Iterate through the list to compare
#     for num in data:
#         if num > largest:
#             largest = num

#     print("The largest number is:", largest)

# print_largest(number_list)

#Using return: Write a function that takes a list of integers and returns the largest number in the list.
# user_input = input("Enter integers separated by space: ")
# number_list = [int(x) for x in user_input.split()]

# def get_largest(numbers):
#     if not numbers:
#         return None

#     largest = numbers[0]

#     for num in numbers:
#         if num > largest:
#             largest = num

#     return largest
# # Call the return function and store the result
# output = get_largest(number_list)

# print("Returned largest number:", output)
# print("Double the largest number:", output * 2)

#SMALLEST NUMBER
# user_input = input("Enter integers separated by space: ")
# number_list = [int(x) for x in user_input.split()]

# # --- USING PRINT ---
# def print_smallest(numbers):
#     if not numbers:
#         print("List is empty!")
#         return
#     smallest = numbers[0]
#     for num in numbers:
#         if num < smallest:
#             smallest = num
#     print("Smallest number:", smallest)

# print_smallest(number_list)

#-- USING RETURN ---
# def get_smallest(numbers):
#     if not numbers:
#         return None
#     smallest = numbers[0]
#     for num in numbers:
#         if num < smallest:
#             smallest = num
#     return smallest
# output = get_smallest(number_list)

# print("Returned smallest number:", output)
# print("Double the smallest number:", output * 2)


#ELEMENT EXISTENCE

nums = [int(x) for x in input("1. Enter list items: ").split()]
target = int(input("2. Enter target element to search: "))
# --- USING PRINT ---
# def print_element_exists(nums, target):
#     found = False
#     for item in nums:
#         if item == target:
#             found = True
#             break
#     if found:
#         print("Found")
#     else:
#         print("Not Found")
# print_element_exists(nums, target)

# --- USING RETURN ---
def check_element_exists(nums, target):
    for item in nums:
        if item == target:
            return True
    return False

print(check_element_exists(nums, target))

