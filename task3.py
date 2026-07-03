#A user is registering on your website and accidentally types their email with extra spaces at the beginning and end: email = "   alex@gmail.com   ". Write a piece of code to clean this input and extract only the valid email ID.
# email= "   alex@gmail.com   " 
# cleaned_email = email.strip()
# print(cleaned_email)

#You are building a secure web crawler. Given a URL string url = "https://xyz.com", write a line of code to verify if the website protocol starts with "https".
# url= "https://xyz.com"
# is_secure= url.startswith("https")
# print(is_secure)

#A Python script needs to clean up server log files. Given the line log_entry = "[ERROR]===System Crash===", write a line of code to strip away only the trailing = characters from the right side.
# log_entry = "[ERROR]===System Crash==="
# cleaned_log= log_entry.rstrip("=")
# print(cleaned_log)

#A user uploads a file named document = "final_report.pdf". Write a piece of code to check if this file ends with the appropriate ".pdf" extension.
# document = "final_report.pdf"
# is_pdf= document.endswith(".pdf")
# print(is_pdf)

#You are building a search bar for an e-commerce store. A user searches for "IPHONE", but the database inventory holds the item as "iphone". Write code to convert the user's search string so it matches the database perfectly, regardless of case.
# user_search= "IPHONE"
# database_inventory= "iphone"
# correct_search= user_search.lower()
# if correct_search== database_inventory:
#  print("Match found! Displaying iphones")
# else:
#  print("Items not found.")

#You are designing a text terminal for a checkout counter. The price of an item is price = "450". Write code to right-justify this price inside a 10-character wide block so it aligns perfectly with other receipts.
# price= "450"
# aligned_price= price.rjust(10)
# print(aligned_price)

#A user submits a chat message containing a banned word: msg = "This software has a nasty bug". Write code to automatically replace the word "bug" with the word "feature".
# msg="This software has a nasty bug."
# new_msg= msg.replace("bug","feature")
# print(new_msg)

#You are writing an automated script to read a Python file. Given a line of text line = "# This is a comment line", write code to check if the line starts with a comment symbol.
# line = "# This is a comment line"
# is_comment= line.startswith("#")
# print(is_comment)

#An API returns a web domain formatted as domain = "www.google.com". Write a single line of code using a strip method to remove the "www." prefix from the left side.
# domain = "www.google.com"
# cleaned_domain= domain.lstrip("w.")
# print(cleaned_domain)

#You are programming a digital scoreboard for a retro arcade game. The current score is score = "75". Write code to pad it with leading zeros using a justification method so it displays as a 5-digit number (00075).
# score= "75"
# display_score= score.rjust(5,"0")
# print(display_score)

#An e-commerce website needs to generate clean URL paths. Given a product title title = "blue running shoes", write code to replace all spaces with dashes (-) to make it look like "blue-running-shoes".
# title = "blue running shoes"
# clean_url= title.replace(" ","-")
# print(clean_url)

#A script reads a secure authentication key from a text file, but it includes an accidental newline character at the end: key = "KEY123XYZ\n". Write a line of code to safely clean this string so only "KEY123XYZ" remains.
# key = "KEY123XYZ\n"
# cleaned_key= key.rstrip()
# print(cleaned_key)

#A system admin wants all server names to stand out in a console report. Given server = "sub-domain-01", write code to completely convert the name into loud, uppercase letters.
# server = "sub-domain-01"
# loud_server= server.upper()
# print(loud_server)


# username = "guest123"
# username.upper()
# print(username)

#You are building a basic email spam filter. Given a message email_body = "Get rich quick! Click here now!", write a piece of code using a string method to check if the word "Click" exists in the text and get its starting position.
email_body = "Get rich quick! Click here now!"
position = email_body.find("Click")
if position != -1:
 print(f"The word 'Click' exists in the text" )
 print(f"Starting position (index): {position}")
else:print(f"The word 'Click' does not found in the text" )
 
# A system is processing a long text document. Given the text paragraph = "Python is great because python code is easy to read", write code to count exactly how many times the lowercase word "python" appears.
paragraph = "Python is great because python code is easy to read"
count = paragraph.count("python")
print(f"The lowercase word 'python' appears {count} time(s). ")

#A registration form requires users to create a username. The system needs to ensure the username contains only letters and numbers, with no special symbols or spaces allowed. Given username = "coder_99", write code to check if it fits this rule.
username = "coder_99"
if username.isalnum():
 print("Valid username")
else:
 print("Invalid username")

#A website allows users to input their birth year. Given the user's input birth_year = "2005", write a line of code to verify if the string consists entirely of numbers before converting it to an integer.
# birth_year = "2005"
# if birth_year.isdigit():

#You are building a forum where users accidentally type titles in all lowercase, like blog_title = "10 tips for learning python". Write code to format this string so that the very first letter of the sentence is capitalized, but the rest remains lowercase.
blog_title = "tips for learning python"
formatted_title = blog_title.capitalize()
print(formatted_title)

#A banking application wants to check if a user is shouting their chat message. Given chat = "HELP ME PLEASE!!", write code to check if all the alphabetical characters in the message are completely in uppercase.
chat = "HELP ME PLEASE!!"
if chat.isupper():
 print("The user is shouting!!")
else:
 print("The user is not shouting!!")



 

 

