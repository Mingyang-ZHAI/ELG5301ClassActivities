
# Create a list and assign it to a variable
original_list = [1, 2, 3]

# Create an alias by assigning the list to another variable
alias_list = original_list

# Modify the list through one alias
alias_list.append(4)

# Print both variables to show that they refer to the same list
print("Original list:", original_list)  # Output: [1, 2, 3, 4]
print("Alias list:", alias_list)        # Output: [1, 2, 3, 4]


# --------------------------------------------
# Create a list
my_list = [1, 2, 3]

# Append a list (the entire list is added as a single element)
my_list.append([4, 5])
print(my_list)  # Output: [1, 2, 3, [4, 5]]

# Reset the list
my_list = [1, 2, 3]

# Extend the list with another list (each element is added individually)
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]


# --------------------------------------------

def check_number(num):
    if num > 0:
        print("The number is positive.")
    else:
        if num == 0:
            print("The number is zero.")
        else:
            print("The number is negative.")

# Example usage
check_number(10)  # Output: The number is positive.
check_number(0)   # Output: The number is zero.
check_number(-5)  # Output: The number is negative.

# --------------------------------------------


# Global dictionary to store names and grades
student_records = {}

def add_name(name):
    if name not in student_records:
        student_records[name] = []
        print(f"Added name: {name}")
    else:
        print(f"{name} already exists.")

def add_grade(name, grade):
    if name in student_records:
        student_records[name].append(grade)
        print(f"Added grade {grade} to {name}")
    else:
        print(f"{name} does not exist. Please add the name first.")

def print_records():
    print("All names and grades:")
    for name, grades in student_records.items():
        print(f"{name}: {grades}")

# Example usage
# Add names
add_name("Alice")
add_name("Bob")

# Add grades to existing names
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 88)

# Print all names and grades
print_records()

# --------------------------------------------

# Global variable
global_var = "I am a global variable"

def my_function():
    # Local variable
    local_var = "I am a local variable"
    
    # Accessing global variable inside the function
    print(global_var)
    
    # Accessing local variable inside the function
    print(local_var)

# Calling the function
my_function()

# Accessing global variable outside the function
print(global_var)

# Trying to access local variable outside the function will cause an error
# Uncommenting the following line will raise a NameError
# print(local_var)


# --------------------------------------------


# Global variable
x = "I am a global variable"

def my_function():
    # Local variable with the same name as the global variable
    x = "I am a local variable"
    
    # Accessing the local variable inside the function
    print("Inside the function:", x)

# Calling the function
my_function()

# Accessing the global variable outside the function
print("Outside the function:", x)

# --------------------------------------------


class StudentRecord:
    def __init__(self):
        self.records = {}  # Dictionary to store names and grades
    
    def add_name(self, name):
        if name not in self.records:
            self.records[name] = []
            print(f"Added name: {name}")
        else:
            print(f"{name} already exists.")
    
    def add_grade(self, name, grade):
        if name in self.records:
            self.records[name].append(grade)
            print(f"Added grade {grade} to {name}")
        else:
            print(f"{name} does not exist. Please add the name first.")
    
    def print_records(self):
        print("All names and grades:")
        for name, grades in self.records.items():
            print(f"{name}: {grades}")

# Create an instance of StudentRecord
student_record = StudentRecord()

# Add names
student_record.add_name("Alice")
student_record.add_name("Bob")

# Add grades to existing names
student_record.add_grade("Alice", 90)
student_record.add_grade("Alice", 85)
student_record.add_grade("Bob", 88)

# Print all names and grades
student_record.print_records()


# --------------------------------------------
