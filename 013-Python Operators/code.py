# 💻 Practical Coding

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)


# 🔢 Precedence Example 1

a = 8
b = 2

result = a + b * 3

print(result)


# 📥 Precedence Example 2 (Using Parentheses)

x = 10
y = 5

print(x + y * 2)
print((x + y) * 2)


# 🧮 Arithmetic Operators - ➕ Addition "+"

print(10 + 5)
print(25 + 15)
print(100 + 250)


price = 100
tax = 15

total = price + tax

print(total)


first_number = 25
second_number = 35
third_number = 40

total = first_number + second_number + third_number

print(total)


# ➖ Subtraction "-"

print(20 - 5)
print(100 - 35)
print(50 - 75)


balance = 500
payment = 125

remaining = balance - payment

print(remaining)


# ✖️ Multiplication "*"

print(5 * 4)
print(10 * 8)
print(7 * 6)


price = 25
quantity = 4

total = price * quantity

print(total)


length = 10
width = 6

area = length * width

print(area)


# ➗ Division "/"

print(10 / 2)
print(15 / 3)
print(7 / 2)


total = 250
people = 5

share = total / people

print(share)


distance = 120
time = 3

speed = distance / time

print(speed)


# 🔢 Modulus "%"

print(10 % 3)
print(20 % 4)
print(25 % 7)


number = 18

print(number % 2)


number = 17

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


number = 24

if number % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 3")


number = 25

if number % 5 == 0:
    print("Divisible by 5")


# ⚡ Exponentiation "**"

print(2 ** 3)
print(5 ** 2)
print(10 ** 3)


base = 4
power = 3

result = base ** power

print(result)


side = 5

area = side ** 2

print(area)


# 📉 Floor Division "//"

print(10 // 3)
print(20 // 6)
print(25 // 4)


total_items = 17
boxes = 5

items_per_box = total_items // boxes

print(items_per_box)


print(13 / 5)
print(13 // 5)


print(-13 / 5)
print(-13 // 5)


# 🔁 Division "/" vs Floor Division "//"

a = 17
b = 4

print(a / b)
print(a // b)


a = 25
b = 6

regular = a / b
floor = a // b

print(regular)
print(floor)


minutes = 135

hours = minutes // 60
remaining_minutes = minutes % 60

print(hours)
print(remaining_minutes)


# 📥 Assignment Operators - "="

x = 100

print(x)


name = "Python"
language = name

print(language)


# "+="

x = 10

x += 5

print(x)


score = 50

score += 10
score += 15

print(score)


# "-="

x = 20

x -= 7

print(x)


balance = 500

balance -= 100
balance -= 75

print(balance)


# "*="

x = 5

x *= 4

print(x)


price = 25

price *= 3

print(price)


# "/="

x = 20

x /= 4

print(x)


distance = 100

distance /= 2

print(distance)


# "%="

x = 17

x %= 5

print(x)


number = 25

number %= 4

print(number)


# "//="

x = 17

x //= 5

print(x)


items = 29

items //= 4

print(items)


# "**="

x = 3

x **= 3

print(x)


number = 2

number **= 5

print(number)


# 🦫 Walrus Operator ":="

numbers = [10, 20, 30, 40]

if (count := len(numbers)) > 3:
    print(count)


text = "Python"

if (length := len(text)) > 5:
    print(length)


numbers = [5, 10, 15, 20]

if (total := sum(numbers)) > 40:
    print(total)


text = "Programming"

if (length := len(text)) >= 10:
    print(f"Length: {length}")


# 🔀 Ternary Operator / Conditional Expression

age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)


number = 15

result = "Even" if number % 2 == 0 else "Odd"

print(result)


temperature = 30

message = "Hot" if temperature > 25 else "Cold"

print(message)


score = 85

result = "Pass" if score >= 50 else "Fail"

print(result)


number = -5

result = "Positive" if number > 0 else "Not positive"

print(result)


# 🔍 Comparison Operators - "=="

x = 10
y = 10

print(x == y)


password = "Python123"

print(password == "Python123")


# "!="

x = 10
y = 20

print(x != y)


number = 15

print(number != 10)


# ">"

print(10 > 5)
print(5 > 10)


score = 85

print(score > 50)


# "<"

print(5 < 10)
print(10 < 5)


age = 16

print(age < 18)


# ">="

print(10 >= 10)
print(15 >= 10)
print(5 >= 10)


score = 50

if score >= 50:
    print("Pass")


# "<="

print(10 <= 10)
print(5 <= 10)
print(15 <= 10)


age = 18

if age <= 18:
    print("Allowed")


# 🔗 Chaining Comparison Operators

x = 5

print(1 < x < 10)


x = 15

print(1 < x < 10)


score = 75

print(0 <= score <= 100)


temperature = 20

print(10 <= temperature <= 30)


number = 50

if 1 <= number <= 100:
    print("Valid")


age = 25

if 18 <= age <= 60:
    print("Age is within the range")


# 🧠 Logical Operators - 🟢 "and"

age = 25
score = 80

print(age >= 18 and score >= 50)


age = 16
score = 80

print(age >= 18 and score >= 50)


number = 12

print(number > 5 and number < 20)


username_exists = True
password_correct = True

if username_exists and password_correct:
    print("Login successful")


# 🟡 "or"

age = 16
has_permission = True

print(age >= 18 or has_permission)


number = 5

print(number == 5 or number == 10)


number = 20

print(number < 10 or number > 15)


# 🔴 "not"

is_ready = True

print(not is_ready)


is_active = False

print(not is_active)


number = 10

print(not number > 20)


# 🪵 Combining Logical Operators

age = 25
score = 90
has_permission = True

result = age >= 18 and score >= 50 and has_permission

print(result)


age = 16
has_permission = False

result = age >= 18 or has_permission

print(result)


number = 15

result = (number > 10 and number < 20) or number == 100

print(result)


# 🆔 Identity Operators - 🔷 "is"

x = [1, 2, 3]
y = x

print(x is y)


x = {"a": 1}
y = x

print(x is y)


# 🔶 "is not"

x = [1, 2, 3]
y = [1, 2, 3]

print(x is not y)


x = [10, 20]
y = [10, 20]

print(x is not y)


# 🆚 "is" vs "=="

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)


x = [1, 2, 3]
y = x

print(x == y)
print(x is y)


x = {"a": 1}
y = {"a": 1}

print(x == y)
print(x is y)


# 🛒 Membership Operators - 📥 "in"

numbers = [10, 20, 30, 40]

print(20 in numbers)


numbers = [10, 20, 30, 40]

print(50 in numbers)


colors = ("red", "green", "blue")

print("green" in colors)


numbers = {10, 20, 30}

print(30 in numbers)


# 📤 "not in"

numbers = [10, 20, 30]

print(50 not in numbers)


numbers = [10, 20, 30]

print(20 not in numbers)


colors = ("red", "green", "blue")

print("yellow" not in colors)


# 🧵 Membership in Strings

text = "Python Programming"

print("Python" in text)


text = "Python Programming"

print("Java" in text)


text = "Python"

print("P" in text)
print("p" in text)


text = "Programming"

print("gram" in text)


text = "Python"

print("Java" not in text)


# ⚡ Bitwise Operators - 🟢 Bitwise AND "&"

print(6 & 3)


print(12 & 10)


x = 7
y = 3

print(x & y)


# 🟡 Bitwise OR "|"

print(6 | 3)


print(12 | 10)


x = 5
y = 2

print(x | y)


# 🔵 Bitwise XOR "^"

print(6 ^ 3)


print(12 ^ 10)


x = 7
y = 3

print(x ^ y)


# 🔴 Bitwise NOT "~"

print(~5)


print(~10)


x = 7

print(~x)


# 🔄 Left Shift "<<"

print(3 << 1)


print(3 << 2)


print(3 << 3)


x = 5

print(x << 2)


# 🔄 Right Shift ">>"

print(12 >> 1)


print(12 >> 2)


print(20 >> 2)


x = 32

print(x >> 3)


# 📥 Bitwise Assignment Operators - "&="

x = 6

x &= 3

print(x)


# "|="

x = 6

x |= 3

print(x)


# "^="

x = 6

x ^= 3

print(x)


# "<<="

x = 3

x <<= 2

print(x)


# ">>="

x = 16

x >>= 2

print(x)


# 🔢 Operator Precedence

result = 10 + 5 * 2

print(result)


result = (10 + 5) * 2

print(result)


result = 100 - 20 / 5

print(result)


result = (100 - 20) / 5

print(result)


result = 2 + 3 * 4 ** 2

print(result)


result = (2 + 3) * 4 ** 2

print(result)


# ⬅️ Left-to-Right Evaluation

result = 20 - 5 + 3

print(result)


result = 100 / 5 * 2

print(result)


result = 10 + 5 - 3 + 2

print(result)


result = 50 // 4 * 2

print(result)


# 🧩 Combined Operator Practice

x = 10
y = 3

result = (x + y) * 2

print(result)


price = 50
quantity = 4
discount = 20

total = price * quantity
final_price = total - discount

print(final_price)


number = 24

if number % 2 == 0 and number > 10:
    print("Valid number")


score = 85

if 0 <= score <= 100 and score >= 50:
    print("Valid passing score")


number = 15

result = (
    "Positive even"
    if number > 0 and number % 2 == 0
    else "Positive odd"
    if number > 0
    else "Negative"
)

print(result)


numbers = [10, 20, 30, 40, 50]

if (count := len(numbers)) > 3 and 30 in numbers:
    print(f"Count: {count}")


x = 10
y = 20

print(x < y and y <= 20)


numbers = [5, 10, 15, 20]
number = 15

if number in numbers and number > 10:
    print("Number found")


x = 8

if x % 2 == 0:
    print("Even")
elif x % 3 == 0:
    print("Divisible by 3")
else:
    print("Other")


a = 10
b = 20
c = 30

result = a < b < c

print(result)


x = 5
y = 10

result = x * 2 + y // 2

print(result)


number = 17

quotient = number // 5
remainder = number % 5

print("Quotient:", quotient)
print("Remainder:", remainder)


base = 2
exponent = 5

result = base ** exponent

print(result)


x = 10

x += 5
x *= 2
x -= 10
x //= 2

print(x)


number = 12

is_valid = number >= 10 and number <= 20

print(is_valid)


text = "Python Operators"

print("Python" in text)
print("Java" not in text)


numbers = [10, 20, 30]

x = numbers
y = [10, 20, 30]

print(x == y)
print(x is y)


a = 6
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(~a)


number = 4

left = number << 2
right = number >> 1

print(left)
print(right)