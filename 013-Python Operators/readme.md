## 1. What Are Operators?

**Operators** are special symbols or keywords used to perform operations on values and variables.

### 📝 Example:

```python
x = 10
y = 3
print(x + y)
```

- **Output:** `13`

### 🔍 Key Concepts:

- `x` and `y` are **operands**.
- `+` is the **operator**.
- `x + y` is an **expression**.

### 📋 Main Types of Python Operators:

| Operator Type | Purpose |
| --- | --- |
| **Arithmetic** | Perform mathematical operations |
| **Assignment** | Assign or update values |
| **Comparison** | Compare values |
| **Logical** | Combine or reverse conditions |
| **Identity** | Check whether two variables refer to the same object |
| **Membership** | Check whether a value exists inside a collection |
| **Bitwise** | Perform operations on binary bits |

---

## 2. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Name | Description |
| --- | --- | --- |
| `+` | Addition | Adds two values |
| `-` | Subtraction | Subtracts one value from another |
| `*` | Multiplication | Multiplies two values |
| `/` | Division | Performs regular division |
| `%` | Modulus | Returns the remainder |
| `**` | Exponentiation | Raises a value to a power |
| `//` | Floor Division | Divides and rounds down |

### 📝 Code Examples:

```python
# Addition
x = 10
y = 5
print(x + y)  # Output: 15

# Subtraction
x = 10
y = 5
print(x - y)  # Output: 5

# Multiplication
x = 10
y = 5
print(x * y)  # Output: 50

# Division
x = 10
y = 4
print(x / y)  # Output: 2.5

# Modulus
x = 10
y = 3
print(x % y)  # Output: 1

# Exponentiation
x = 2
y = 4
print(x ** y)  # Output: 16

# Floor Division
x = 10
y = 3
print(x // y)  # Output: 3
```

---

## 3. Division (`/`) vs Floor Division (`//`)

- The `/` operator performs **regular division** and always returns a `float`.
- The `//` operator performs **floor division** and returns the floor of the result (rounded down).

### 📝 Examples with whole & decimal results:

```python
print(12 / 4)   # Output: 3.0
print(12 // 4)  # Output: 3

print(13 / 5)   # Output: 2.6
print(13 // 5)  # Output: 2
```

⚠️ **Important:** Floor division rounds **down**, not simply toward zero.

```python
print(-13 / 5)   # Output: -2.6
print(-13 // 5)  # Output: -3
```

---

## 4. Assignment Operators

Assignment operators are used to assign or update values stored in variables.

### 📝 Math Assignment Examples:

```python
# "=" Basic Assignment
x = 10
print(x)  # Output: 10

# "+=" Addition Assignment (equivalent to: x = x + 5)
x = 10
x += 5
print(x)  # Output: 15

# "-=" Subtraction Assignment (equivalent to: x = x - 3)
x = 10
x -= 3
print(x)  # Output: 7

# "*=" Multiplication Assignment
x = 10
x *= 2
print(x)  # Output: 20

# "/=" Division Assignment
x = 10
x /= 4
print(x)  # Output: 2.5

# "%=" Modulus Assignment
x = 10
x %= 3
print(x)  # Output: 1

# "//=" Floor Division Assignment
x = 10
x //= 3
print(x)  # Output: 3

# "**=" Exponentiation Assignment
x = 2
x **= 3
print(x)  # Output: 8
```

### 📝 Bitwise Assignment Examples:

```python
# "&=" Bitwise AND Assignment
x = 6
x &= 3
print(x)  # Output: 2

# "|=" Bitwise OR Assignment
x = 6
x |= 3
print(x)  # Output: 7

# "^=" Bitwise XOR Assignment
x = 6
x ^= 3
print(x)  # Output: 5

# ">>=" Bitwise Right Shift Assignment
x = 8
x >>= 2
print(x)  # Output: 2

# "<<=" Bitwise Left Shift Assignment
x = 3
x <<= 2
print(x)  # Output: 12
```

---

## 5. Walrus Operator (`:=`)

The **Walrus Operator** `:=` is called the *assignment expression operator*. It allows you to assign a value to a variable while using that value as part of an expression simultaneously.

### 📝 Example:

```python
numbers = [10, 20, 30, 40]

if (count := len(numbers)) > 3:
    print(count)
```

- **Output:** `4`

💡 **Here, `count := len(numbers)` does two things:**

1. Calculates `len(numbers)`.
2. Assigns the result directly to `count` so it can be used immediately inside the condition.

---

## 6. Ternary Operator / Conditional Expression

Python's ternary syntax allows you to choose between two values depending on a specific condition.

### 📑 Syntax:

```python
value_if_true if condition else value_if_false
```

### 📝 Example:

```python
age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)
```

- **Output:** `Adult`

🔍 **Note:** The condition is checked first. If `True`, the first value is returned; if `False`, the value after `else` is returned.

---

## 7. Comparison Operators

Comparison operators are used to compare two values, and the result is always a Boolean (`True` or `False`).

| Operator | Meaning |
| --- | --- |
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

### 📝 Code Examples:

```python
x = 10
y = 10
print(x == y)  # Equal To -> Output: True

x = 10
y = 5
print(x != y)  # Not Equal -> Output: True

x = 10
y = 5
print(x > y)   # Greater Than -> Output: True

x = 10
y = 5
print(x < y)   # Less Than -> Output: False

x = 10
y = 10
print(x >= y)  # Greater Than or Equal -> Output: True

x = 10
y = 15
print(x <= y)  # Less Than or Equal -> Output: True
```

⚠️ **Important Distinction:**

- `=` is for **Assignment** (assigns a value to a variable).
- `==` is for **Value Comparison** (checks if two values are equal).

---

## 8. Chaining Comparison Operators

Python allows multiple comparisons to be chained together seamlessly, which is useful to check if a value falls within a range.

### 📝 Examples:

```python
x = 5
print(1 < x < 10)  # Means: 1 < x and x < 10
# Output: True

score = 75
print(0 <= score <= 100)
# Output: True
```

---

## 9. Logical Operators

Logical operators are used to combine or reverse conditions.

| Operator | Meaning |
| --- | --- |
| `and` | `True` if **both** conditions are true |
| `or` | `True` if **at least one** condition is true |
| `not` | Reverses the Boolean result |

### 📝 Code Examples:

```python
# "and" Operator (Both must be True)
age = 25
has_ticket = True
print(age >= 18 and has_ticket)  # Output: True

# "or" Operator (At least one must be True)
temperature = 30
print(temperature < 0 or temperature > 25)  # Output: True

# "not" Operator (Inverts the Boolean)
is_ready = True
print(not is_ready)  # Output: False
```

---

## 10. Identity Operators

Identity operators are used to check whether two variables refer to the **exact same object in memory**.

| Operator | Meaning |
| --- | --- |
| `is` | Returns `True` if it is the same object |
| `is not` | Returns `True` if it is not the same object |

### 📝 Code Examples:

```python
# "is" Operator
x = [1, 2, 3]
y = x
print(x is y)  # Output: True (Both point to the same list object)

# "is not" Operator
x = [1, 2, 3]
y = [1, 2, 3]
print(x is not y)  # Output: True (They contain the same values but are separate objects)
```

---

## 11. `==` vs `is`

This is a critical distinction in Python:

- `==` checks whether two objects have **equal values**.
- `is` checks whether two variables refer to the **exact same object identity**.

### 📝 Comparison Example:

```python
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)  # Output: True (Equal contents)
print(x is y)  # Output: False (Different objects in memory)

# If both point to the same item:
z = x
print(x == z)  # Output: True
print(x is z)  # Output: True
```

> 💡 **Rule to Remember:** Use `==` when comparing values, and use `is` when checking object identity.
> 

---

## 12. Membership Operators

Membership operators are used to check whether a value exists inside another collection object (Lists, Tuples, Sets, Strings).

| Operator | Meaning |
| --- | --- |
| `in` | `True` if value exists inside the object |
| `not in` | `True` if value does not exist inside the object |

### 📝 Code Examples:

```python
numbers = [10, 20, 30]

print(20 in numbers)      # Output: True
print(50 not in numbers)  # Output: True
```

---

## 13. Membership in Strings

The `in` and `not in` operators work with strings and are **case-sensitive**.

### 📝 Code Examples:

```python
text = "Python"

print("P" in text)  # Output: True
print("z" in text)  # Output: False

# Testing Case-Sensitivity
print("p" in text)  # Output: False
```

---

## 14. Bitwise Operators

Bitwise operators work with integers at the level of their binary representation.

| Operator | Name | Description |
| --- | --- | --- |
| `&` | AND | Sets a bit to `1` if both bits are `1` |
| `|` | OR | Sets a bit to `1` if at least one bit is `1` |
| `^` | XOR | Sets a bit to `1` if the bits are different |
| `~` | NOT | Inverts all the bits |
| `<<` | Left Shift | Shifts bits to the left (Multiplies by $2^n$ for positive ints) |
| `>>` | Right Shift | Shifts bits to the right (Integer division by $2^n$ for positive ints) |

## ⚡ Bitwise AND "&"

```python
x = 6
y = 3

print(x & y)

# Output:
# 2
```

### 🔍 Binary representation:

```
6 = 0110
3 = 0011
---------
    0010
```

👉 `"0010"` is `2`.

---

## ⚡ Bitwise OR "|"

```python
x = 6
y = 3

print(x | y)

# Output:
# 7
```

---

## ⚡ Bitwise XOR "^"

```python
x = 6
y = 3

print(x ^ y)

# Output:
# 5
```

---

## ⚡ Bitwise NOT "~"

```python
x = 5

print(~x)

# Output:
# -6
```

`~` is a bitwise operator. It is different from the logical operator: `not`

---

## 🔄 Left Shift "<<"

```python
x = 3

print(x << 2)

# Output:
# 12
```

> 💡 For positive integers, shifting left by `"n"` positions is equivalent to multiplying by `"2 ** n"`.
> 

---

## 🔄 Right Shift ">>"

```python
x = 12

print(x >> 2)

# Output:
# 3
```

> 💡 For positive integers, shifting right by `"n"` positions is equivalent to integer division by `"2 ** n"`.
> 

---

## 🔢 15. Operator Precedence

Operator precedence determines the order in which Python evaluates operators in an expression.

### 📝 For example:

```python
result = 100 + 5 * 3

print(result)

# Output:
# 115
```

Multiplication is performed before addition:

- `5 * 3 = 15`
- `100 + 15 = 115`

### 📥 If parentheses are used:

```python
result = (100 + 5) * 3

print(result)

# Output:
# 315
```

> 📌 Parentheses change the order of evaluation.
> 

---

## 16. Precedence Order

A simplified precedence order from higher to lower is:

| Priority | Operators |
| --- | --- |
| **1** | `()` |
| **2** | `**` |
| **3** | `+x`, `-x`, `~x` |
| **4** | `*`, `/`, `//`, `%` |
| **5** | `+`, `-` |
| **6** | `<<`, `>>` |
| **7** | `&` |
| **8** | `^` |
| **9** | `|` |
| **10** | Comparisons, `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in` |
| **11** | `not` |
| **12** | `and` |
| **13** | `or` |

The operators higher in the table are evaluated before operators lower in the table.

---

## ⬅️ 17. Left-to-Right Evaluation

When operators have the same precedence, Python generally evaluates them from left to right.

```python
result = 5 + 4 - 7 + 3

print(result)

# Output:
# 5
```

### 🔍 The expression is evaluated as:

- `5 + 4 = 9`
- `9 - 7 = 2`
- `2 + 3 = 5`

Parentheses can always be used when you want to make the intended order explicit.

```python
result = (5 + 4) - (7 + 3)

print(result)

# Output:
# -1
```

---

## 📋 Quick Summary

| Category | Main Operators |
| --- | --- |
| **Arithmetic** | `+`, `-`, `*`, `/`, `%`, `**`, `//` |
| **Assignment** | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `//=`, `**=` |
| **Walrus** | `:=` |
| **Comparison** | `==`, `!=`, `>`, `<`, `>=` |
| **Precedence** | Determines evaluation order |

### Most Important Distinctions

- `=` Assignment
- `==` Value comparison
- `is` Object identity
- `in` Membership
- `and` Both conditions
- `or` At least one condition
- `not` Reverse a Boolean result
- `/` Regular division
- `//` Floor division
- `%` Remainder
- `*` Power