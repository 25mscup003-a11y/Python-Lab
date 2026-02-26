# Read number of terms from the user
n = int(input("Enter the number of terms: "))

# First two Fibonacci numbers
a = 0
b = 1

print("Fibonacci Series:")

# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        print(c)
        a = b
        b = c
