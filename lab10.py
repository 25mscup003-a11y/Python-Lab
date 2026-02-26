# Accept list of numbers from user
numbers = input("Enter numbers separated by spaces: ")

# Convert input string into list of integers
num_list = list(map(int, numbers.split()))

# Create empty list for even numbers
even_numbers = []

# Filter even numbers using loop
for num in num_list:
    if num % 2 == 0:
        even_numbers.append(num)

# Print even numbers
print("Even numbers:", even_numbers)
