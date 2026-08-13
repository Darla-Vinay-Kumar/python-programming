# operators.py

# =========================
# Python Operators
# =========================

# 1. Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


# 2. Comparison Operators
x = 10
y = 20

print("\nComparison Operators")
print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater Than:", x > y)
print("Less Than:", x < y)
print("Greater Than or Equal:", x >= y)
print("Less Than or Equal:", x <= y)


# 3. Assignment Operators
number = 10

print("\nAssignment Operators")

number += 5
print("+= :", number)

number -= 3
print("-= :", number)

number *= 2
print("*= :", number)

number /= 4
print("/= :", number)

number //= 2
print("//= :", number)

number %= 3
print("%= :", number)


# 4. Logical Operators
is_devops_engineer = True
has_aws_experience = True
is_python_expert = False

print("\nLogical Operators")
print("AND:", is_devops_engineer and has_aws_experience)
print("OR:", is_devops_engineer or is_python_expert)
print("NOT:", not is_python_expert)


# 5. Membership Operators
skills = ["AWS", "Docker", "Kubernetes", "Terraform"]

print("\nMembership Operators")
print("AWS in skills:", "AWS" in skills)
print("Python in skills:", "Python" in skills)
print("Python not in skills:", "Python" not in skills)


# 6. Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("\nIdentity Operators")
print("a is b:", a is b)
print("a is c:", a is c)
print("a is not c:", a is not c)


# 7. Bitwise Operators
a = 10
b = 3

print("\nBitwise Operators")
print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)