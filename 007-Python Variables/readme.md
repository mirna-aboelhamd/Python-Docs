# Python Variables

A variable is a container used to store a value. Python does not require a separate command to declare a variable. A variable is created when a value is assigned to it.

```python
x = 10
language = "Python"

print(x)
print(language)

# Output:
# 10
# Python
```

---

## 🗒️ Changing Variable Values

A variable can be assigned a new value after it has been created. Its data type can also change.

```python
value = 10
print(value)

value = "Python"
print(value)

# Output:
# 10
# Python
# (The variable "value" first stores an integer and then stores a string)
```

---

## 🗒️ Casting

Casting is used to convert a value to a specific data type. It is useful when a value needs to be used as a specific type.

| Function | Purpose |
| --- | --- |
| `str()` | Converts a value to a string |
| `int()` | Converts a value to an integer |
| `float()` | Converts a value to a float |

```python
number = 10

text_value = str(number)
integer_value = int(number)
decimal_value = float(number)

print(text_value)
print(integer_value)
print(decimal_value)

# Output:
# 10
# 10
# 10.0
```

---

## 🗒️ Single or Double Quotes

String values can be written using either single quotes or double quotes. Both quotation styles can be used to create strings.

```python
language = "Python"
framework = 'Django'

print(language)
print(framework)

# Output:
# Python
# Django
```

---

## 🗒️ Case-Sensitive Variables

Python is case-sensitive, so uppercase and lowercase letters are treated as different characters.

```python
value = 10
Value = 20

print(value)
print(Value)

# Output:
# 10
# 20
# ("value" and "Value" are two different variables)
```

---

## 🗒️ Python Variable Names & Rules

### Naming Rules

- **Start:** Must start with a letter or an underscore `_`.
- **Numbers:** Cannot start with a number.
- **Characters:** Can contain letters, numbers, and underscores.
- **Case:** Is case-sensitive.
- **Keywords:** Cannot be a Python keyword.

### Valid vs Invalid Examples

```python
# ✅ Valid Variable Names
data = 100
data_value = 200
_data = 300
data2 = 400

# ❌ Invalid Variable Names (Will cause SyntaxError)
2data = 100
data-value = 200
data value = 300
```

---

## 🗒️ Multi-Word Variable Names

Variable names containing multiple words can be written using different naming styles.

### Camel Case

Each word after the first starts with a capital letter.

```python
dataValue = 100
```

### Pascal Case

Each word starts with a capital letter.

```python
DataValue = 100
```

### Snake Case

Words are separated by underscores.

```python
data_value = 100
```

---

## 🗒️ Assign Multiple Values

### Many Values to Multiple Variables

The number of variables must match the number of values.

```python
x, y, z = 10, 20, 30

print(x)
print(y)
print(z)

# Output:
# 10
# 20
# 30
```

### One Value to Multiple Variables

```python
x = y = z = 0

print(x)
print(y)
print(z)

# Output:
# 0
# 0
# 0
```

### Unpack a Collection

Unpacking means extracting values from a collection and assigning them to variables. Each variable receives the corresponding value from the collection.

```python
coordinates = [10, 20, 30]

x, y, z = coordinates

print(x)
print(y)
print(z)

# Output:
# 10
# 20
# 30
```

---

## 🗒️ Output Variables with `print()`

The `print()` function is used to display variable values.

```python
status = "active"
print(status)

# Output:
# active
```

### Output Multiple Variables with Commas

Using commas allows different data types to be printed together and separates them with a space.

```python
width = 100
height = 200
print(width, height)

language = "Python"
version = 3.14
print(language, version)

# Output:
# 100 200
# Python 3.14
```

### Output Multiple Variables with `+`

The `+` operator can be used to combine string variables. If spaces are needed, they must be included in the strings.

```python
part1 = "Data"
part2 = "Base"
print(part1 + part2)

part1_space = "Data "
part2_space = "Base"
print(part1_space + part2_space)

# Output:
# DataBase
# Data Base
```

### Using `+` with Numbers

With numeric values, `+` performs addition.

```python
x = 10
y = 20
print(x + y)

# Output:
# 30
```

### ❌ Combining a String and a Number

A string and a number cannot be combined directly using `+`. This produces a `TypeError`. To print different data types together, use commas instead.

```python
language = "Python"
version = 3

# This line will crash:
# print(language + version)

# Correct way:
print(language, version)

# Output:
# Python 3
```

---

## 🗒️ Global vs Local Variables

### Global Variables

A variable created outside a function is called a global variable. It can be accessed inside a function.

```python
status = "active"

def check_status():
    print(status)

check_status()

# Output:
# active
```

### Local Variables

A variable created inside a function is called a local variable. It can only be used inside that function. The local variable does not change the global one.

```python
status = "active"

def check_status():
    status = "inactive"
    print(status)

check_status()
print(status)

# Output:
# inactive
# active
```

### The `global` Keyword

Used when a function needs to create or modify a global variable from inside a scope.

```python
# 1. Creating a Global Variable Inside a Function
def set_status():
    global status
    status = "active"

set_status()
print(status)

# Output:
# active

# 2. Modifying an Existing Global Variable
current_status = "inactive"

def update_status():
    global current_status
    current_status = "active"

update_status()
print(current_status)

# Output:
# active
```