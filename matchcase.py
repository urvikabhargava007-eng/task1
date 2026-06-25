number = int(input("enter a number (1-7): "))
match number:
 case 1:
  print("monday")
 case 2:
  print("tuesday")
 case 3:
  print("wednesday")
 case 4:
  print("thursday")
 case 5:
  print("friday")
 case 6:
  print("saturday")
 case 7:
  print("sunday")
 case _:
  print("invalid number")

amount = int(input("enter the amount: "))
match amount:
 case 20:
  print("You will get 200ml coldrink.")
 case 50:
  print("You will get 750ml coldrink")
 case 100:
  print("You will get 1l coldrink")
 case _:
  print("No coldrink")

month = int(input("enter the month: "))
match month:
  case 1: 
   print("January-31 Days")
  case 2:
   print("February-28/29 Days")
  case 3:
   print("March-31 Days")
  case 4:
   print("April-30 Days")
  case 5:
   print("May-31 Days")
  case 6:
   print("June-30 Days")
  case 7:
   print("July-31 Days")
  case 8:
   print("August-31 Days")
  case 9:
   print("September-30 Days")
  case 10:
   print("October-31 Days")
  case 11:
   print("November-30 Days")
  case 12:
   print("December-31 Days")
  
#CALCULATOR
input1 = int(input("Enter first number.:"))
input2 = int(input("Enter second number.:"))
op = input("Enter operator (+,-,*,/):")
match op:
 case '+':
  print(input1+input2)
 case '-':
  print(input1-input2)
 case '*':
  print(input1*input2)
 case '/':
  print(input1/input2)
 case _:
  print("Invalid input")
 