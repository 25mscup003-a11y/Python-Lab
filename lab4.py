# Accept a string from the user
text = input("Enter a string: ")

# Initialize counters
vowels = 0
consonants = 0
digits = 0
special_chars = 0

# Define vowels
vowel_set = "aeiouAEIOU"

# Loop through each character in the string
for char in text:
    if char.isalpha():  # Check if character is a letter
        if char in vowel_set:
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():  # Check if character is a digit
        digits += 1
    else:  # If not letter or digit, it's a special character
        special_chars += 1

# Display the results
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special Characters:", special_chars)
