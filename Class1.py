print("Hello World!")


PI = 3.14
PI = 3.15
print(PI)

# --------------------------------------------


# Define the string
name = "Mingyang Zhai"

# Count the length of the string
length = len(name)

# Print the length
print(f"The length of the name 'Mingyang Zhai' is {length} characters.")


# --------------------------------------------


# Prompt the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the division
if num2 != 0:
    result = num1 / num2
    print(f"The result of dividing {num1} by {num2} is {result}.")
else:
    print("Error: Division by zero is not allowed.")


# --------------------------------------------

# Initialize the sum variable
total_sum = 0.0

while True:
    user_input = input("Enter a number (or type 'stop' to finish): ")
    
    if user_input.lower() == "stop":
        break
    
    try:
        number = float(user_input)
        total_sum += number
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Print the total sum
print(f"The total sum of the numbers entered is {total_sum}.")


# --------------------------------------------


# Initialize the dictionary to store students' names and grades
student_grades = {}

while True:
    student_name = input("Enter the student's full name (or type 'stop' to finish): ")
    
    if student_name.lower() == "stop":
        break
    
    try:
        grade = float(input(f"Enter the grade for {student_name}: "))
        student_grades[student_name] = grade
    except ValueError:
        print("Invalid input. Please enter a valid grade.")

# Print all students' names and their corresponding grades
print("Students and their grades:")
for name, grade in student_grades.items():
    print(f"{name}: {grade}")


