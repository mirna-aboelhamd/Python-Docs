- Python Strings
    
    ## 1. What Is a String & Displaying
    
    A string is a sequence of characters surrounded by quotation marks. You can use either single or double quotes (both are equivalent). Strings can contain letters, numbers, symbols, spaces, and special characters.
    
    ```python
    print("Hello")
    print('Hello')
    
    # Output:
    # Hello
    # Hello
    ```
    
    Use the `print()` function to display a string:
    
    ```python
    print("Python is easy to learn.")
    
    # Output:
    # Python is easy to learn.
    ```
    
    ---
    
    ## 2. Quotes Inside Strings & Escape Characters
    
    You can use quotation marks inside a string if the inner quotation mark is different from the outer quotation mark. If you use the same quotation mark inside and outside, you must use a backslash `\` as an escape character.
    
    ```python
    print("It's a programming language")
    print('He said "Hello".')
    print("He said \"Hello\".")
    
    # Output:
    # It's a programming language
    # He said "Hello".
    # He said "Hello".
    ```
    
    ---
    
    ## 3. Assigning a String to a Variable
    
    You can store a string in a variable just like other data types using the assignment operator `=`.
    
    ```python
    language = "Python"
    print(language)
    
    # Output:
    # Python
    ```
    
    ---
    
    ## 4. Multiline Strings
    
    You can create a string that spans multiple lines using three single quotes `'''` or three double quotes `"""`. The line breaks are preserved automatically.
    
    ```python
    text = """This is a multiline string"""
    print(text)
    
    # Output:
    # This is a multiline string
    ```
    
    ---
    
    ## 5. String Indexing
    
    Each character in a string has an index. Python uses zero-based indexing (the first character is `0`). Positive indexing starts from the beginning, while negative indexing starts from the end (the last character is `-1`).
    
    ### 📊 Indexing Reference Table
    
    | Character | P | y | t | h | o | n |
    | --- | --- | --- | --- | --- | --- | --- |
    | **Positive Index** | 0 | 1 | 2 | 3 | 4 | 5 |
    | **Negative Index** | -6 | -5 | -4 | -3 | -2 | -1 |
    
    ```python
    text = "Python"
    print(text[0])
    print(text[1])
    print(text[5])
    print(text[-1])
    print(text[-2])
    
    # Output:
    # P
    # y
    # n
    # n
    # o
    ```
    
    *⚠️ Note: Negative indexing does NOT reverse the string.*
    
    ---
    
    ## 6. Slicing Strings
    
    You can return a range of characters using slicing.
    
    - **Syntax:** `string[start:end]` *(The start index is included, the end index is excluded)*
    - **Slice From Start:** Leaving out the start value defaults to `0`.
    - **Slice To End:** Leaving out the end value continues to the very end of the string.
    
    ```python
    text = "Python"
    print(text[0:2])
    print(text[2:5])
    print(text[:4])
    print(text[2:])
    print(text[-4:-1])
    
    # Output:
    # Py
    # tho
    # Pyth
    # thon
    # tho
    ```
    
    ---
    
    ## 7. Modifying Strings (String Methods)
    
    **Important Rule:** Strings in Python are **immutable** (cannot be changed). String methods always return a *new* value; they do not modify the original string.
    
    ```python
    text = "python"
    new_text = text.upper()
    print(text)
    print(new_text)
    
    # Output:
    # python
    # PYTHON
    ```
    
    ### 🛠️ Common Modifying Methods
    
    - **`upper()`** ➔ Converts characters to uppercase.
    
    ```python
    text = "python"
    print(text.upper()) # Output: PYTHON
    ```
    
    - **`lower()`** ➔ Converts characters to lowercase.
    
    ```python
    text = "PYTHON"
    print(text.lower()) # Output: python
    ```
    
    - **`strip()`** ➔ Removes whitespace from the beginning and end (but not between words).
    
    ```python
    text = " Python "
    print(text.strip()) # Output: Python
    ```
    
    - **`replace()`** ➔ Replaces a specified part of a string with a new value.
    
    ```python
    text = "I like Java"
    print(text.replace("Java", "Python")) # Output: I like Python
    ```
    
    - **`split()`** ➔ Splits a string into a list of substrings using a specified separator (defaults to whitespace).
    
    ```python
    text = "Python is powerful"
    print(text.split()) # Output: ['Python', 'is', 'powerful']
    
    csv_text = "apple,banana,orange"
    print(csv_text.split(",")) # Output: ['apple', 'banana', 'orange']
    ```
    
    ---
    
    ## 8. String Concatenation
    
    Combining strings together using the `+` operator. To add a space, you must include a literal `" "`.
    
    ```python
    first = "Hello"
    second = "World"
    result = first + second
    print(result) # Output: HelloWorld
    
    result_with_space = first + " " + second
    print(result_with_space) # Output: Hello World
    ```
    
    ---
    
    ## 9. String Formatting & F-Strings
    
    You cannot directly concatenate a string and a number using `+` (it causes a `TypeError`). Instead, use **F-Strings** (introduced in Python 3.6).
    
    - **Syntax:** `f"Text {variable}"`
    
    ```python
    age = 25
    print(f"I am {age} years old.")
    # Output: I am 25 years old
    
    language = "Python"
    version = 3.14
    print(f"{language} version {version}")
    # Output: Python version 3.14
    
    # Expressions Inside F-Strings
    price = 50
    quantity = 3
    print(f"Total: {price * quantity}")
    # Output: Total: 150
    
    # F-String Modifiers
    price = 19.5
    print(f"Price: {price:.2f}")
    # Output: Price: 19.50
    ```
    
    ---
    
    ## 10. Escape Characters Reference
    
    A backslash `\` followed by a character allows you to insert illegal characters into a string.
    
    ```python
    # New Line \n
    print("Python\nProgramming")
    # Output:
    # Python
    # Programming
    
    # Tab \t
    print("Python\tProgramming")
    # Output: Python	Programming
    ```
    
    ### 📊 Common Escape Sequences
    
    | Escape Sequence | Meaning |
    | --- | --- |
    | `\'` | Single quote |
    | `\"` | Double quote |
    | `\\` | Backslash |
    | `\n` | New line |
    | `\r` | Carriage return |
    | `\t` | Tab |
    | `\b` | Backspace |
    
    ---
    
    ## 11. Comprehensive String Methods Cheat Sheet
    
    ### 🔠 Case Conversion
    
    | Method | Description |
    | --- | --- |
    | `capitalize()` | Converts the first character to uppercase |
    | `casefold()` | Converts string to lowercase for case-insensitive comparison |
    | `lower()` | Converts the string to lowercase |
    | `swapcase()` | Swaps uppercase to lowercase and vice versa |
    | `title()` | Converts the first character of each word to uppercase |
    | `upper()` | Converts the string to uppercase |
    
    ### 🔍 Searching and Counting
    
    | Method | Description |
    | --- | --- |
    | `count()` | Counts how many times a value occurs |
    | `find()` | Finds the first occurrence of a value |
    | `index()` | Finds the position of a value |
    | `rfind()` | Finds the last occurrence of a value |
    | `rindex()` | Finds the position of the last occurrence of a value |
    | `startswith()` | Checks whether the string starts with a specified value |
    | `endswith()` | Checks whether the string ends with a specified value |
    
    ### 🚦 Checking String Content
    
    | Method | Description |
    | --- | --- |
    | `isalnum()` | Checks whether all characters are alphanumeric |
    | `isalpha()` | Checks whether all characters are alphabetic |
    | `isascii()` | Checks whether all characters are ASCII |
    | `isdecimal()` | Checks whether all characters are decimal characters |
    | `isdigit()` | Checks whether all characters are digits |
    | `isidentifier()` | Checks whether the string is a valid identifier |
    | `islower()` | Checks whether all cased characters are lowercase |
    | `isnumeric()` | Checks whether all characters are numeric |
    | `isprintable()` | Checks whether all characters are printable |
    | `isspace()` | Checks whether all characters are whitespace |
    | `istitle()` | Checks whether the string follows title-case rules |
    | `isupper()` | Checks whether all cased characters are uppercase |
    
    ### ✂️ Splitting and Joining
    
    | Method | Description |
    | --- | --- |
    | `join()` | Joins elements of an iterable into a single string |
    | `partition()` | Splits the string into three parts around a separator |
    | `rpartition()` | Partitions around the last occurrence of a separator |
    | `rsplit()` | Splits the string from the right |
    | `split()` | Splits the string into a list |
    | `splitlines()` | Splits the string at line boundaries |
    
    ### 🧹 Removing and Replacing
    
    | Method | Description |
    | --- | --- |
    | `lstrip()` | Removes whitespace from the left side |
    | `rstrip()` | Removes whitespace from the right side |
    | `strip()` | Removes whitespace from both sides |
    | `replace()` | Replaces a specified value |
    
    ### 📐 Formatting and Alignment
    
    | Method | Description |
    | --- | --- |
    | `center()` | Centers the string |
    | `format()` | Formats specified values |
    | `format_map()` | Formats the string using a mapping |
    | `ljust()` | Left-aligns the string |
    | `rjust()` | Right-aligns the string |
    | `zfill()` | Adds zeros to the beginning of the string |
    
    ### 🔐 Translation, Encoding & Others
    
    | Method | Description |
    | --- | --- |
    | `encode()` | Encodes the string |
    | `maketrans()` | Creates a translation table |
    | `translate()` | Translates characters using a translation table |
    | `expandtabs()` | Sets the tab size |