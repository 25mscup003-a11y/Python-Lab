# main.py

import os
from strength import is_strong

# Get current script directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_FILE = os.path.join(BASE_DIR, "passwords.txt")
OUTPUT_FILE = os.path.join(BASE_DIR, "weak_passwords.txt")


def check_passwords():
    try:
        with open(INPUT_FILE, "r") as infile, open(OUTPUT_FILE, "w") as outfile:
            for line in infile:
                password = line.strip()

                if password and not is_strong(password):
                    outfile.write(password + "\n")

        print("Password check completed.")
        print(f"Weak passwords saved to {OUTPUT_FILE}")

    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} not found.")


if __name__ == "__main__":
    check_passwords()