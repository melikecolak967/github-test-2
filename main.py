def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a * b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero")
    else:
        raise ValueError("Invalid operation")

