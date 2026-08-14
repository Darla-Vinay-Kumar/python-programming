# if_else.py

# =========================
# Python if, elif and else
# =========================

# 1. Simple if statement
age = 20

if age >= 18:
    print("You are eligible to vote.")


# 2. if-else statement
age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# 3. if-elif-else statement
marks = 75

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")


# 4. Multiple conditions using logical operators
age = 25
has_id = True

if age >= 18 and has_id:
    print("Access granted.")
else:
    print("Access denied.")


# 5. Using OR condition
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend.")
else:
    print("It's a working day.")


# 6. Nested if statement
username = "admin"
password = "python123"

if username == "admin":
    if password == "python123":
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("Invalid username.")


# 7. Checking positive, negative or zero
number = -10

if number > 0:
    print("Positive number.")
elif number < 0:
    print("Negative number.")
else:
    print("Zero.")


# 8. Checking even or odd
number = 10

if number % 2 == 0:
    print("Even number.")
else:
    print("Odd number.")


# 9. User input with if-else
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible.")
else:
    print("You are not eligible.")


# 10. Practical DevOps example
cpu_usage = 85

if cpu_usage >= 90:
    print("Critical: CPU usage is very high.")
elif cpu_usage >= 75:
    print("Warning: CPU usage is high.")
else:
    print("CPU usage is normal.")