# Iterate through a dictionary and print all its keys
# my_dict = {"apple": 5, "banana": 3, "cherry": 8}

# for key in my_dict:
#     print(key)

# # Iterate through a dictionary and print all its values
# my_dict = {"apple": 5, "banana": 3, "cherry": 8}

# for value in my_dict.values():
#     print(value)

#Print both keys and values side-by-side using a loop
# my_dict = {"apple": 5, "banana": 3, "cherry": 8}

# for key, value in my_dict.items():
#     print(f"{key}: {value}")

#Given items and prices, calculate total cost of all items using a loop
# a = {
#     "car" : 1000,
#     "shoes" : 500,
#     "house" : 10000,
#     "phone" : 5000
#     }
# total = 0
# for x in a:
#     total += a[x]

# print(total)





#Create a dictionary where keys are 1–5 and values are squares using a while loop
# squares_dict = {}
# num = 1
# while num <= 5:
#     squares_dict[num] = num ** 2
#     num += 1
# print(squares_dict)


#Filter out items where the value is an even number into a new dictionary
# original_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# even_dict = {}

# for key, value in original_dict.items():
#     if value % 2 == 0:
#         even_dict[key] = value

# print(even_dict)

#Find the key with the highest value using a loop
# scores = {"A": 85, "B": 92, "C": 78}
# b = list(scores.keys())
# largest = b[0]
# for x in range(1,len(b)):
#     if b[x] > largest:
#         largest = b[x]
# print(f"{largest} : {scores[largest]}")


#Swap keys and values using a loop
# old_dict = {"a": 1, "b": 2, "c": 3}
# swapped_dict = {}

# for key, value in old_dict.items():
#     swapped_dict[value] = key

# print(swapped_dict)


#Merge two dictionaries manually using a loop
# dict_a = {"x": 10, "y": 20}
# dict_b = {"y": 30, "z": 40}  

# merged_dict = {}
# for key, value in dict_a.items():
#     merged_dict[key] = value
# for key, value in dict_b.items():
#     merged_dict[key] = value

# print(merged_dict)   

# Loop through numbers 1 to 10 (the tables)
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end=" ")
#     print() 

#WITHOUT LOOPS

#1. Access a Value Safely without a KeyError.
user = {"name": "Alice", "age": 25}
print(user.get("name"))         
print(user.get("age"))         
print(user.get("city", "N/A"))


#2. Find the Total Number of Key-Value Pairs.
user = {"a": 1, "b": 2, "c": 3}
print(len(user))


#3. Add or Update a Key-Value Pair.
user = {"name": "Alice"}
user["age"] = 25
user.update({"city": "New York"})

print(user)


#4. Remove a Key and Return Its Values.
user = {"name": "Alice", "age": 25}
removed_age = user.pop("age")

print(removed_age) 
print(user)         


#5. Check if a Key Exists without a loop.
user = {"name": "Alice", "age": 25}
print("name" in user)  
print("email" in user)  


#6. Clear All Items from a Dictionary.
user = {"name": "Alice", "age": 25, "city": "London"}
user.clear()

print(user) 

#7. Merge Two Dictionaries in a Single Line.
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 99, "c": 4} 

merged = dict1 | dict2

print(merged)


#8. Extract All Keys into a List without using loop.
user = {"name": "Alice", "age": 25, "city": "London"}

keys_list = list(user.keys())
values_list = list(user.values())
both = list(user.items())

print("keys:", keys_list)
print("values:", values_list) 
print(both)


#9. Create a Dictionary from a List of Keys with Default Value 0.
keys = ["apples", "bananas", "cherries"]

counts = dict.fromkeys(keys, 0)

print(counts)


#10. Create a Shallow Copy of a Dictionary.
original = {"a": 1, "b": 2}

shallow_copy = original.copy()

print(shallow_copy) 

#Quick Cheat Sheet
# TaskBuilt-in -- Syntax / Method
# safe Read -- d.get(key, default)
# Count Pairs -- len(d)
# Remove & Return -- d.pop(key)
# Check Key Existence -- key in d
# Merge -- d1 | d2
# Default Dict from Keys -- dict.fromkeys(keys, 0)


