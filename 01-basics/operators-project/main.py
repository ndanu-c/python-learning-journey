
# ==========================================
# SIMPLE PYTHON CALCULATOR
# A beginner Python project
# ==========================================

# Ask the user to enter the first number
# Convert the input from a string to a float
x = float(input("Enter first number "))

# Ask the user to enter an operator
# strip() removes unnecessary spaces around the input
operator = input("Enter operator ").strip()

# Ask the user to enter the second number
# Convert the input from a string to a float
y = float(input("Enter second number "))


# Check whether the user is attempting an operation
# that requires division by a non-zero number
if y == 0 and (operator == "/" or operator == "%" or operator == "//"):
    answer = None

else:
    # Perform addition
    if operator == "+":
        answer = x + y

    # Perform subtraction
    elif operator == "-":
        answer = x - y

    # Perform multiplication
    elif operator == "*":
        answer = x * y

    # Perform division
    elif operator == "/":
        answer = x / y

    # Find the remainder using modulus
    elif operator == "%":
        answer = x % y

    # Perform exponentiation
    elif operator == "**":
        answer = x ** y

    # Perform floor division
    elif operator == "//":
        answer = x // y

    # Handle operators that are not supported
    else:
        answer = None


# Check whether a valid calculation was performed
if answer is not None:
    # Display the calculation and its result
    print(f"{x} {operator} {y} = {answer}")

else:
    # Display an error message for invalid operations
    print("Invalid operator!")
