# 1. Storing Values

product = "Keyboard"
quantity = 2
price = 25

print(product)
print(quantity)
print(price)


# 2. Changing a Variable

temperature = 20
print(temperature)

temperature = 25
print(temperature)


# 3. Casting

value = "25"
number = int(value)

print(number + 5)


# 4. Multiple Variables

width = 10
height = 5
area = width * height

print(area)


# 5. Multiple Assignment

x, y, z = 10, 20, 30

print(x)
print(y)
print(z)


# 6. One Value to Multiple Variables

x = y = z = 0

print(x)
print(y)
print(z)


# 7. Unpacking a List

dimensions = [100, 200, 300]
width, height, depth = dimensions

print(width)
print(height)
print(depth)


# 8. Printing Multiple Variables

width = 100
height = 200

print(width, height)


# 9. Combining String Variables

file_name = "data"
file_type = ".txt"

print(file_name + file_type)


# 10. Calculating with Variables

price = 50
quantity = 4
total = price * quantity

print(total)


# 11. Global Variable

status = "active"

def show_status():
    print(status)

show_status()


# 12. Local Variable

status = "active"

def check_status():
    status = "inactive"
    print(status)

check_status()
print(status)


# 13. Changing a Global Variable

status = "inactive"

def activate():
    global status
    status = "active"

activate()
print(status)