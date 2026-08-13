# data_types.py

# =========================
# Python Data Types
# =========================

# 1. String
name = "Darla Vinay Kumar"
print("String:", name)
print("Type:", type(name))

# 2. Integer
age = 31
print("Integer:", age)
print("Type:", type(age))

# 3. Float
salary = 411365.50
print("Float:", salary)
print("Type:", type(salary))

# 4. Boolean
is_devops_engineer = True
print("Boolean:", is_devops_engineer)
print("Type:", type(is_devops_engineer))

# 5. List
skills = ["AWS", "Docker", "Kubernetes", "Terraform"]
print("List:", skills)
print("Type:", type(skills))

# 6. Tuple
coordinates = (12.9716, 77.5946)
print("Tuple:", coordinates)
print("Type:", type(coordinates))

# 7. Set
cloud_tools = {"AWS", "Azure", "AWS", "GCP"}
print("Set:", cloud_tools)
print("Type:", type(cloud_tools))

# 8. Dictionary
employee = {
    "name": "Vinay",
    "role": "DevOps Engineer",
    "experience": 4
}
print("Dictionary:", employee)
print("Type:", type(employee))

# 9. None
value = None
print("None:", value)
print("Type:", type(value))

# =========================
# Type Conversion
# =========================

number = "100"

integer_value = int(number)
float_value = float(number)

print("String:", number)
print("Integer:", integer_value)
print("Float:", float_value)

# Integer to String
age = 31
age_string = str(age)

print("Age:", age_string)
print("Type:", type(age_string))