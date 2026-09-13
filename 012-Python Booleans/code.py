# 1. Boolean Values

temperature = 28
print(temperature > 30)
print(temperature == 28)
print(temperature < 20)

# 2. Booleans in "if" Statements — Example 1

battery_level = 75

if battery_level > 20:
    print("System is ready")
else:
    print("Battery is too low")

# 3. Booleans in "if" Statements — Example 2

score = 42

if score >= 50:
    print("Condition passed")
else:
    print("Condition not passed")

# 4. Evaluate Values and Variables — Example 1

status = "active"
quantity = 15

print(bool(status))
print(bool(quantity))

# 5. Evaluate Values and Variables — Example 2

status = ""
quantity = 0

print(bool(status))
print(bool(quantity))

# 6. Most Values Are "True"

print(bool("Python"))
print(bool(100))
print(bool([10, 20]))
print(bool((10, 20)))
print(bool({10, 20}))
print(bool({"mode": "active"}))

# 7. Some Values Are "False"

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool(set()))
print(bool({}))

# 8. Objects Can Evaluate to "False"

class DataContainer:
    def __len__(self):
        return 0

data = DataContainer()
print(bool(data))


class DataContainerValid:
    def __len__(self):
        return 3

data2 = DataContainerValid()
print(bool(data2))

# 9. Functions Can Return a Boolean

def system_ready():
    return True

print(system_ready())


def system_faulty():
    return False

print(system_faulty())

# 10. Using Boolean Function Results in "if" — Example 1

def system_ready():
    return True

if system_ready():
    print("System is ready")
else:
    print("System is not ready")

# 11. Using Boolean Function Results in "if" — Example 2

def system_ready():
    return False

if system_ready():
    print("System is ready")
else:
    print("System is not ready")

# 12. Built-in Functions That Return Boolean — Testing Instances

value = 200
print(isinstance(value, int))

value_str = "200"
print(isinstance(value_str, int))

value_float = 12.5
print(isinstance(value_float, (int, float)))

# 13. Built-in Functions That Return Boolean — Inside Conditionals

value = "Python"

if isinstance(value, str):
    print("Value is a string")
else:
    print("Value is not a string")