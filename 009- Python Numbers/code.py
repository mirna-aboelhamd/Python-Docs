# 1. Updating a Calculation

total = 100
additional = 25

total = total + additional

print(total)


# 2. Using Different Operations with Variables

value = 20

addition = value + 5
subtraction = value - 5
multiplication = value * 2
division = value / 2

print(addition)
print(subtraction)
print(multiplication)
print(division)


# 3. Casting Before a Calculation

input_value = "8"

number = int(input_value)
result = number * number

print(result)


# 4. Multiple Assignment in a Calculation

base, height = 12, 6

area = base * height / 2

print(area)


# 5. Unpacking Coordinates

point = (15, 30)

x, y = point

print(x + y)


# 6. Building a Message from Variables

protocol = "HTTPS"
port = 443

message = protocol + " uses port " + str(port)

print(message)


# 7. Updating a Variable Step by Step

counter = 0

counter = counter + 1
counter = counter + 1
counter = counter + 1

print(counter)


# 8. Local and Global Variables

mode = "production"

def check_mode():
    mode = "testing"
    print(mode)

check_mode()
print(mode)


# 9. Changing a Global Variable

connection = "closed"

def open_connection():
    global connection
    connection = "open"

open_connection()
print(connection)


# 10. Using Multiple Variables Together

start = 10
end = 50
step = 5

result = (end - start) / step

print(result)