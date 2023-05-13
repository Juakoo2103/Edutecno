# This program is a simple calculator.

# Define the functions for addition, subtraction, multiplication, and division.
def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

# Get the user's input for the first number.
print("Enter the first number: ")
first_number = int(input())

# Get the user's input for the second number.
print("Enter the second number: ")
second_number = int(input())

# Display the menu of operations.
print("What operation would you like to perform?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get the user's input for the operation.
operation = int(input())

# Perform the operation on the two numbers.
if operation == 1:
  result = add(first_number, second_number)
elif operation == 2:
  result = subtract(first_number, second_number)
elif operation == 3:
  result = multiply(first_number, second_number)
elif operation == 4:
  result = divide(first_number, second_number)

# Display the result.
print("The result is: " + str(result))