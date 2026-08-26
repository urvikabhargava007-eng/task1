import os

# os.remove("01.md")

# print(dir(os))

# a = os.listdir()
# print(a)

# print(os.path.exists("/onedrive/desktop/pythonprojects/practice.py"))
# print(os.path.isfile("/onedrive/desktop/pythonprojects/"))
#print(os.path.isdir("pythonprojects"))




# Terminal:
    # * if user type ls it will list all the files of the dir
    # * if user type lsfolder it will list all the folders only
    # * if user type lsfiles it will list all the files only
    # * if user type exit stop the terminal

# while True:
#     command  = input("-->")
#     if command == "ls":
#         print(os.listdir())
#     elif command == "lsfolder":
#         data = os.listdir()
#         for x in data:
#             if os.path.isdir(x):
#                 print(x)
#     elif command == "lsfiles":
#         data = os.listdir()
#         for x in data:
#             if os.path.isfile(x):
#                 print(x)
#     elif command == "pyfiles":
#         a = os.listdir()
#         for x in a:
#             if x.endswith(".py"):
#                 print(x)
#     elif command == "jsonfile":
#         a = os.listdir()
#         for x in a:
#             if x.endswith(".json"):
#                 print(x)
#     elif command == "exit":
#         break
#     else:
#         print("invalid command")
