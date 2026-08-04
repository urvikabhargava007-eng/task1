
# 1. How do you filter a list of words to extract only those that start with a vowel (a, e, i, o, u)?
words_1 = ["apple", "banana", "orange", "grape", "umbrella", "kiwi"]
vowel_words = [w for w in words_1 if w and w[0].lower() in "aeiou"]

print(" Words starting with a vowel:")
print(vowel_words)
print("-" * 50)


# 2.How do you create a new list containing the length of each word in a word list?
words_2 = ["python", "list", "comprehension"]
lengths = [len(w) for w in words_2]

print(" Word lengths:")
print(lengths)
print("-" * 50)


# 3. How do you convert all words in a list to uppercase, but only if the word has more than 4 characters?
words_3 = ["cat", "elephant", "dog", "giraffe"]
long_words_upper = [w.upper() for w in words_3 if len(w) > 4]

print(" Words > 4 chars in uppercase:")
print(long_words_upper)
print("-" * 50)


# 4. How do you transform a list of numbers by replacing even numbers with "Even" and odd numbers with "Odd"?
numbers = [1, 2, 3, 4, 5, 6]
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]

print(" Even/Odd replacement:")
print(labels)
print("-" * 50)


# 5. How do you extract non-blank, clean lines from a list of raw string lines read from a file?





#DICIONARY COMPREHENSION

# 1.How do you convert a list of words into a dictionary mapping each word to its character count?
words = ["python", "dictionary", "comprehension"]
word_lengths = {word: len(word) for word in words}

print(" Word character counts:")
print(word_lengths)
print("-" * 50)

# 2. How do you filter an existing dictionary to keep only the key-value pairs where the numeric value is greater than a threshold (e.g., scores >= 80)?
scores = {"Alice": 95, "Bob": 67, "Charlie": 82, "David": 74}
passing_scores = {name: score for name, score in scores.items() if score >= 80}

print(" Filtered scores (>= 80):")
print(passing_scores)
print("-" * 50)


# 3. How do you swap (invert) the keys and values of a dictionary?
code_map = {"A": 1, "B": 2, "C": 3}
inverted_map = {val: key for key, val in code_map.items()}

print(" Inverted keys and values:")
print(inverted_map)
print("-" * 50)

# 4. How do you count the frequency of each unique word in a list of words using a dictionary comprehension?
word_list = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_counts = {word: word_list.count(word) for word in set(word_list)}

print(" Word frequency counts:")
print(word_counts)
print("-" * 50)


# 5. How do you categorize items in a dictionary based on their values (e.g., marking scores as "Pass" or "Fail")?
student_scores = {"Alice": 85, "Bob": 62, "Charlie": 78, "David": 70}
results = {name: ("Pass" if score >= 75 else "Fail")for name, score in student_scores.items()
}

print(" Categorized results:")
print(results)
print("-" * 50)