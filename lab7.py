# Read marks of 5 subjects
print("Enter marks for 5 subjects:")

total = 0
for i in range(1, 6):
    marks = float(input(f"Subject {i}: "))
    total += marks

# Calculate average
average = total / 5

# Determine grade using nested conditions
if average >= 50:  # Pass condition
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"
else:
    grade = "F"

# Display result
print("\nTotal Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)
