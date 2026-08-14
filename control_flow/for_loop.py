# for_loop.py

# =========================
# Python for Loops
# =========================

# 1. Basic for loop
for number in range(1, 6):
    print(number)


# 2. Loop through a list
skills = ["AWS", "Docker", "Kubernetes", "Terraform"]

for skill in skills:
    print(skill)


# 3. Loop through a string
name = "Python"

for character in name:
    print(character)


# 4. Using range()
print("Numbers from 0 to 4:")

for number in range(5):
    print(number)


# 5. Using start and stop
print("Numbers from 1 to 10:")

for number in range(1, 11):
    print(number)


# 6. Using start, stop and step
print("Even numbers:")

for number in range(2, 11, 2):
    print(number)


# 7. Calculate sum
total = 0

for number in range(1, 6):
    total += number

print("Total:", total)


# 8. Multiplication table
number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# 9. if condition inside a for loop
numbers = [10, 15, 20, 25, 30]

for number in numbers:
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")


# 10. break statement
for number in range(1, 11):
    if number == 6:
        break

    print(number)


# 11. continue statement
for number in range(1, 11):
    if number == 5:
        continue

    print(number)


# 12. Nested for loop
for outer in range(1, 4):
    for inner in range(1, 4):
        print(f"Outer: {outer}, Inner: {inner}")


# 13. Loop through a dictionary
employee = {
    "name": "Vinay",
    "role": "DevOps Engineer",
    "experience": 4
}

for key, value in employee.items():
    print(f"{key}: {value}")


# 14. Practical DevOps example
servers = ["web-01", "web-02", "db-01", "cache-01"]

for server in servers:
    print(f"Checking server: {server}")