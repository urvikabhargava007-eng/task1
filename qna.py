#Write a program that forces a user to enter a secure password. The while loop should keep asking for input until the user provides a string that meets all of these criteria:

# At least 8 characters long
# Contains at least one digit (0-9)
# Contains at least one special character (like $, #, or @)

# password = input("Enter a password")
# if len(password) >= 8:
#     ...
# else:
#     print("Password must contain atleast 8 characters.")

password = input("Enter a password: ")
# if len(password) >= 8:
#     if "0" in password or "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password:
#        if "$" in password or "#" in password or "@" in password:
#          print("It is a strong password.")
#        else:
#           print("Password must contain a special character $,#,@.")
#     else:
#         print("Password does not have any number.")
# else:
#     print("Password must contain atleast 8 characters.")

length = 0
has_spl = 0
has_number = 0
for x in password:
    length += 1
    if x == "$" or x == "#" or x == "@":
        has_spl = True
print(length)
print(has_spl)






