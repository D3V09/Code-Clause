def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

print("Simple Calculator")
print("Options:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter option (1/2/3/4) or 'q' to quit: ")

    if choice.lower() == 'q':
        print("Exiting calculator.")
        break

    if choice not in ['1', '2', '3', '4']:
        print("Invalid option. Please try again.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    else:
        result = divide(num1, num2)

    print("Result: ", result)