def calculator():
    # Get user input for numbers and operator
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /, %): ").strip()
    num2 = float(input("Enter the second number: "))

    # Perform the operation based on the operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    elif operator == '%':
        result = num1 % num2
    else:
        return "Invalid operator. Please enter one of the following: +, -, *, /, %."

    return f"The result is: {result}"

# Example usage:
print(calculator())
