import math

class AdvancedCalculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero."

    def power(self, x, y):
        return x ** y

    def square_root(self, x):
        return math.sqrt(x)

    def logarithm(self, x, base):
        return math.log(x, base)

# Create an instance of the AdvancedCalculator class
calculator = AdvancedCalculator()

while True:
    print("\nAdvanced Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '8':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4', '5', '6', '7']:
        x = float(input("Enter the first number: "))

        if choice != '6':  # Square root only requires one input
            y = float(input("Enter the second number: "))

        if choice == '1':
            result = calculator.add(x, y)
            print("Result:", result)
        elif choice == '2':
            result = calculator.subtract(x, y)
            print("Result:", result)
        elif choice == '3':
            result = calculator.multiply(x, y)
            print("Result:", result)
        elif choice == '4':
            result = calculator.divide(x, y)
            print("Result:", result)
        elif choice == '5':
            result = calculator.power(x, y)
            print("Result:", result)
        elif choice == '6':
            result = calculator.square_root(x)
            print("Result:", result)
        elif choice == '7':
            base = float(input("Enter the logarithm base: "))
            result = calculator.logarithm(x, base)
            print("Result:", result)
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
