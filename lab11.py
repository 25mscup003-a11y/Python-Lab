import re

# Ask user for log file name
filename = input("Enter log file name (with .txt): ")

try:
    with open(filename, 'r') as file:
        content = file.read()

        # Regular expression pattern for email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

        # Find all email addresses
        emails = re.findall(email_pattern, content)

        # Remove duplicates (optional)
        unique_emails = set(emails)

        print("\nExtracted Email Addresses:")
        for email in unique_emails:
            print(email)

        print("\nTotal Emails Found:", len(unique_emails))

except FileNotFoundError:
    print("Error: File not found. Please check the filename.")
