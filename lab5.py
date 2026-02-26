# Read a number from the user
number = int(input("Enter a number: "))

# Print multiplication table from 1 to 10
print(f"Multiplication Table of {number}:\n")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
