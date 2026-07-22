#Write a program that asks the user to enter an integer. How should the program handle the situation if the user enters text or a decimal value instead?
while True:
    user_input = input("Please enter an integer: ")
    try:
        number = int(user_input)
        print(f"Success! You entered: {number}")
        break 
    except ValueError:
        print("Invalid input! Please enter a whole number (no decimals or text).\n")

#Create a program that divides two numbers entered by the user. How should the program handle division by zero and invalid numeric input?
try:
    numerator = float(input("Enter the numerator (number to divide): "))
    denominator = float(input("Enter the denominator (number to divide by): "))
    
    result = numerator / denominator
    print(f"Result: {numerator} ÷ {denominator} = {result}")

except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")


#Create a program that accepts a list index from the user and displays the corresponding element. How should the program handle cases where the index is out of range or the input is not a valid integer?
fruits = ["Apple", "Banana", "Cherry", "Dragonfruit", "Elderberry"]

print(f"List: {fruits}")
user_input = input("Enter an index number: ")

try:
    index = int(user_input)
    print(f"Item at index {index}: {fruits[index]}")

except ValueError:
    print("Error: You must type a whole number!")

except IndexError:
    print("Error: That number is outside the list range!")