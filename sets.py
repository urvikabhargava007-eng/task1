#1. Multiply Each Element by 10
numbers = {1, 2, 3, 4, 5}

for num in numbers:
    print(num * 10)


#2. Find the Sum of All Numbers
numbers = {5, 10, 15, 20}
total_sum = 0

for num in numbers:
    total_sum += num

print("Sum:", total_sum)


#3. Count Strings with Length Greater Than 4
words = {"apple", "cat", "banana", "dog", "elephant"}
count = 0

for word in words:
    if len(word) > 4:
        count += 1

print("Count of long words:", count)


#4. Filter Odd Numbers into a New Set
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
odd_numbers = set()

for num in numbers:
    if num % 2 != 0:
        odd_numbers.add(num)

print("Odd numbers set:", odd_numbers)


#5. Combine (Union) a List of Sets into One Set
list_of_sets = [{1, 2}, {2, 3, 4}, {4, 5, 6}]
combined_set = set()

for s in list_of_sets:
    combined_set = combined_set.union(s)

print("Combined set:", combined_set)


#Without Loops 

#1. Total Number of Unique Elements
my_set = {10, 20, 30, 40}
print(len(my_set)) 


#2. Common Elements in Two Sets
#Using the .intersection() method or the & operator:

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

common = set_a.intersection(set_b)
# Or: common = set_a & set_b

print(common)


#3. Add Single vs. Multiple Elements
my_set = {1, 2}
my_set.add(3)

my_set.update([4, 5, 6])

print(my_set) 


#4. Combine All Unique Elements from Both Sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}

all_unique = set_a.union(set_b)
print(all_unique) 


#5. Remove an Element Without Raising an Error if Missing
my_set = {1, 2, 3}

my_set.discard(99) 
my_set.discard(2)   

print(my_set)

#6. Check if One Set is a Subset of Another
small_set = {1, 2}
big_set = {1, 2, 3, 4}
print(small_set.issubset(big_set)) 

#7. Remove All Elements (Empty the Set)
my_set = {1, 2, 3, 4, 5}
my_set.clear()
print(my_set)