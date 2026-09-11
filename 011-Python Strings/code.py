# 1. Creating & Displaying Strings

# Example 1: Using Double Quotes
text = "Python"
print(text)

# Example 2: Using Single Quotes
text = 'Programming'
print(text)

# Displaying Strings
message = "Welcome to Python"
print(message)


# 2. Quotes Inside Strings & Escape Characters

# Example 1: Double Quotes Outside
text = "Python is called a 'programming language'"
print(text)

# Example 2: Single Quotes Outside
text = 'Python is called a "programming language"'
print(text)

# Escape Characters for Quotes
text = "The message says \"Python is useful\""
print(text)


# 3. Assigning Strings & Multiline Strings

# Assigning Strings to Variables
language = "Python"
topic = "Strings"
print(language)
print(topic)

# Multiline Strings
text = """Python
is
easy"""
print(text)


# 4. String Indexing & Slicing

# String Indexing
text = "Python"
print(text[0])
print(text[2])
print(text[5])

# Practical Example
code = "PYTHON"
print(code[1])
print(code[3])

# Negative Indexing
text = "Python"
print(text[-1])
print(text[-2])
print(text[-3])

# Basic String Slicing
text = "Python"
print(text[0:2])
print(text[2:5])

# Slice From the Start
text = "Programming"
print(text[:6])

# Slice to the End
text = "Programming"
print(text[6:])

# Negative Slicing
text = "Programming"
print(text[-5:-1])

text2 = "Python"
print(text2[-4:])


# 5. Built-in String Methods

# upper() - Convert to Uppercase
text = "python strings"
print(text.upper())

# lower() - Convert to Lowercase
text = "PYTHON STRINGS"
print(text.lower())

# strip() - Remove outer whitespace
text = "  Python  "
print(text.strip())

# replace() - Replace values
text = "Python is simple"
result = text.replace("simple", "powerful")
print(result)

# split() - Split string into a list
text = "Python is useful"
words = text.split()
print(words)

# split() with a custom separator
data = "Python,Java,SQL"
items = data.split(",")
print(items)


# 6. String Concatenation

first = "Python"
second = "Programming"
result = first + second
print(result)

# Concatenation With a Space
result = first + " " + second
print(result)

# Combining Multiple Strings
language = "Python"
topic = "Strings"
level = "Beginner"
result = language + " - " + topic + " - " + level
print(result)


# 7. F-Strings & Formatting

# Using F-Strings
quantity = 5
print(f"Quantity: {quantity}")

# Multiple F-String Variables
language = "Python"
level = "Beginner"
print(f"Language: {language}")
print(f"Level: {level}")

# F-Strings With Calculations
price = 20
quantity = 3
print(f"Total: {price * quantity}")

# F-Strings With Expressions
first_number = 10
second_number = 5
print(f"Result: {first_number + second_number}")

# F-String Formatting With .2f
price = 19.5
print(f"Price: {price:.2f}")

average = 87.4567
print(f"Average: {average:.2f}")


# 8. Common Escape Sequences

# \' Single Quote
text = 'It\'s Python'
print(text)

# \" Double Quote
text = "Python is \"easy\" to learn"
print(text)

# \\ Backslash
path = "folder\\files"
print(path)

# \n New Line
text = "Python\nStrings"
print(text)

# \t Tab Formatting
text = "Python\tStrings"
print(text)


# 9. More String Methods & Validations

# capitalize()
text = "python"
print(text.capitalize())

# title()
text = "python string methods"
print(text.title())

# swapcase()
text = "Python STRINGS"
print(text.swapcase())

# count()
text = "banana"
print(text.count("a"))

# find()
text = "Python Programming"
print(text.find("Programming"))
print(text.find("Java"))

# startswith() & endswith()
text = "Python Programming"
print(text.startswith("Python"))

file_name = "report.txt"
print(file_name.endswith(".txt"))

# Content Check Methods
print("Python123".isalnum())
print("Python 123".isalnum())
print("Python".isalpha())
print("12345".isdigit())
print("python".islower())
print("PYTHON".isupper())
print("   ".isspace())


# 10. Advanced Methods

# join() - Combine iterable into one string
items = ["Python", "SQL", "Git"]
result = " - ".join(items)
print(result)

# partition() - Splits around a separator into 3 parts
text = "Python-Programming"
result = text.partition("-")
print(result)

# splitlines() - Split multiline text into a list
text = """Python
SQL
Git"""
print(text.splitlines())

# lstrip() & rstrip()
print("  Python".lstrip())
print("Python  ".rstrip())

# center(), ljust(), rjust()
text = "Python"
print(text.center(12, "-"))
print(text.ljust(10, "-"))
print(text.rjust(10, "-"))

# zfill() - Pad with leading zeros
number = "25"
print(number.zfill(5))

# casefold() - Case-insensitive lowercasing
text = "PYTHON"
print(text.casefold())

# encode() - Encodes string into bytes
text = "Python"
print(text.encode())


# 11. Practical Combined Examples

# Example 1: Cleaning and Formatting Text
text = "   python programming   "
clean_text = text.strip()
formatted_text = clean_text.title()
print(formatted_text)

# Example 2: Checking a File Extension
file_name = "report.pdf"
if file_name.endswith(".pdf"):
    print("PDF file")

# Example 3: Splitting and Cleaning Data
text = "  python,sql,git  "
clean_text = text.strip()
items = clean_text.split(",")
print(items)

# Example 4: Search and Replace
text = "Python is useful"
if text.find("Python") != -1:
    text = text.replace("useful", "powerful")
print(text)