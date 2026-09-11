# 1. Text Type — str

language = "Python"
file_type = "text"

print(language)
print(file_type)


# 2. Numeric Types

# int

items = 10
score = 85

print(items)
print(score)


# float

price = 25.50
average = 87.5

print(price)
print(average)


# complex

number = 4 + 3j

print(number)


# 3. Sequence Types

# list

languages = ["Python", "Java", "C++"]

print(languages)
print(languages[0])


# tuple

coordinates = (10, 20, 30)

print(coordinates)
print(coordinates[1])


# range

numbers = range(5)

for number in numbers:
    print(number)


# 4. Mapping Type — dict

product = {
    "name": "Laptop",
    "price": 500,
    "quantity": 3
}

print(product["name"])
print(product["price"])


# 5. Set Types

# set

numbers = {1, 2, 3, 4}

print(numbers)


# frozenset

numbers = frozenset({1, 2, 3, 4})

print(numbers)


# 6. Boolean Type — bool

is_open = True
is_empty = False

print(is_open)
print(is_empty)


# 7. Binary Types

# bytes

data = b"Python"

print(data)


# bytearray

data = bytearray(5)

print(data)


# memoryview

data = bytes(5)
view = memoryview(data)

print(view)


# 8. None Type — NoneType

result = None

print(result)


# Getting the Data Type — type()

language = "Python"
items = 10
price = 25.50

print(type(language))
print(type(items))
print(type(price))


# Setting a Specific Data Type

# str, int, float

language = str("Python")
items = int(10)
price = float(25.50)

print(language)
print(items)
print(price)


# list, tuple, range

languages = list(("Python", "Java", "C++"))
coordinates = tuple((10, 20, 30))
numbers = range(5)

print(languages)
print(coordinates)
print(numbers)


# dict, set, frozenset

product = dict(name="Laptop", price=500)
numbers = set((1, 2, 3, 4))
fixed_numbers = frozenset((1, 2, 3, 4))

print(product)
print(numbers)
print(fixed_numbers)


# bool, bytes, bytearray, memoryview

is_open = bool(1)
data = bytes(5)
mutable_data = bytearray(5)
view = memoryview(bytes(5))

print(is_open)
print(data)
print(mutable_data)
print(view)