# Read a number from the user
number = int(input("Enter a number: "))

# Store original number (optional, for display)
original = number

# Initialize reversed number
reversed_num = 0

# Reverse the number using while loop
while number != 0:
    digit = number % 10          # Get last digit
    reversed_num = reversed_num * 10 + digit
    number = number // 10        # Remove last digit

# Display the result
print("Reversed number is:", reversed_num)
