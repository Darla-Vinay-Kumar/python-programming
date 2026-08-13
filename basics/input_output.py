# input_output.py

# =========================
# Python Input and Output
# =========================

# 1. Basic Output
print("Hello, Python!")
print("Welcome to Python programming.")


# 2. Printing Multiple Values
name = "Vinay"
age = 31

print("Name:", name)
print("Age:", age)


# 3. Using sep
print("AWS", "Docker", "Kubernetes", sep=" | ")


# 4. Using end
print("Hello", end=" ")
print("World")


# 5. Taking User Input
name = input("Enter your name: ")

print("Hello,", name)


# 6. Input is Always a String
age = input("Enter your age: ")

print("Age:", age)
print("Data type:", type(age))


# 7. Converting Input to Integer
age = int(input("Enter your age: "))

print("Your age is:", age)
print("Next year you will be:", age + 1)


# 8. Taking Float Input
salary = float(input("Enter your salary: "))

print("Salary:", salary)


# 9. Taking Multiple Inputs
first_name, last_name = input(
    "Enter your first and last name: "
).split()

print("First Name:", first_name)
print("Last Name:", last_name)


# 10. Formatted Output - f-string
name = "Vinay"
experience = 4
role = "DevOps Engineer"

print(
    f"My name is {name}. "
    f"I have {experience} years of experience as a {role}."
)


# 11. Basic Calculation with User Input
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

print("Sum:", number1 + number2)
print("Difference:", number1 - number2)
print("Product:", number1 * number2)
print("Division:", number1 / number2)