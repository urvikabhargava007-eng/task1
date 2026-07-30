# f = open('onedrive/desktop/pythonprojects/abc.txt')
# print(f.read())
# f.close()

# f = open('onedrive/desktop/pythonprojects/abc.txt', 'w')
# print(f.write("I love my Country"))
# f.close()
# 
# f = open('onedrive/desktop/pythonprojects/abc.txt')
# print(f.readlines())
# f.close()

# f = open('onedrive/desktop/pythonprojects/abc.txt')
# print(f.readable())
# f.close()

# f = open('onedrive/desktop/pythonprojects/abc.txt')
# print(f.readline())
# f.close()


#1.Read a text file and count the total number of vowels in it?
# with open ("onedrive/desktop/pythonprojects/sample.txt" , "r") as m:
#     data = m.read()
#     i=0
#     vowels=0
#     while i<len(data):
#         if data[i] in "aeiouAEIOU":
#             vowels += 1
#         i += 1
# print(vowels)

#2.Count the total number of words in a file?
# Open and read the file
# with open("onedrive/desktop/pythonprojects/sample.txt", "r") as file:
#     content = file.read()
    
# # .split() splits string by any whitespace (spaces, tabs, newlines)
# words = content.split()

# #3. Print the total line count
# print("Total number of words:", len(words))

# with open("onedrive/desktop/pythonprojects/sample.txt", "r") as file:
#     lines = file.readlines()

# print("Total number of lines:", len(lines))

#4. Display only the lines in a file that contain the word "India"?
# longest_line = ""
# max_word_count = 0


#5. Find the longest line in a text file?
# with open("onedrive/desktop/pythonprojects/sample.txt", "r") as file:
#     for line in file:
#         words = line.split()
        
#         if len(words) > max_word_count:
#             max_word_count = len(words)
#             longest_line = line

# print("Line with the most words:")
# print(longest_line.strip())
# print("Total words:", max_word_count)

#6.Take a word from the user and count how many times that word appears across an entire file?
# search_word = input("Enter the word to search: ").lower()

# try:
#     with open("onedrive/desktop/pythonprojects/sample.txt", "r") as file:
#         content = file.read().lower()
        
#     words = content.split()
    
#     count = words.count(search_word)
    
#     print(f"The word '{search_word}' appears {count} times in the file.")

# except FileNotFoundError:
#     print("Error: The file 'sample.txt' was not found.")

#7. Take 5 words from the user and count how many times each word appears across an entire file? 
# words_to_find = []
# print("Enter 5 words to search:")
# for i in range(1, 6):
#     word = input(f"Word {i}: ").strip().lower()
#     words_to_find.append(word)

# with open("onedrive/desktop/pythonprojects/sample.txt", "r") as file:
#     content = file.read().lower()
#     file_words = content.split()

# print("\n--- Search Results ---")
# for word in words_to_find:
#     count = file_words.count(word)
#     print(f"'{word}': {count} time(s)")

#8. Copy non-blank lines from a source file into a clean list of data?
# clean_list = []

# with open("onedrive/desktop/pythonprojects/sample.txt", "r") as file:
#     for line in file:
#         cleaned_line = line.strip()
        
#         if cleaned_line != "":
#             clean_list.append(cleaned_line)

# print("Cleaned List:", clean_list)
# print("Total non-blank lines:", len(clean_list))

#9. Count the total number of blank lines in a text file?




