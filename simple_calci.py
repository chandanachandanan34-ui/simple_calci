# Basic Calculator Program

print("----- BASIC CALCULATOR -----")

# Taking inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)\n")

choice = input("Enter your choice (1/2/3/4): ")

# Performing operations
if choice == '1':
    print("Result =", num1 + num2)

elif choice == '2':
    print("Result =", num1 - num2)

elif choice == '3':
    print("Result =", num1 * num2)

elif choice == '4':
    if num2 == 0:
        print("Error! Division by zero is not allowed.")
    else:
        print("Result =", num1 / num2)

else:
    print("Invalid Choice! Please select 1–4.")
