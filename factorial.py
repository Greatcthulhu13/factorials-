def factorial(n):
    return 1 if n ==  0 or n == 1 else n * factorial(n - 1)

num = int(input("Enter a number to calculate its factorial: "))

print(f"Factorial of {num} is: {factorial(num)}")
