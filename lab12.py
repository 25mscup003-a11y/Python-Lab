import hashlib

def calculate_hash(file_path, algorithm="sha256"):
    hash_func = hashlib.new(algorithm)

    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        print("Error: File not found.")
        return None


# ---- Main Program ----
file_path = input("Enter file path: ")
known_hash = input("Enter known malicious hash: ").lower()

# Choose algorithm based on hash length
if len(known_hash) == 32:
    algorithm = "md5"
elif len(known_hash) == 64:
    algorithm = "sha256"
else:
    print("Invalid hash length! Provide MD5 (32 chars) or SHA256 (64 chars).")
    exit()

calculated_hash = calculate_hash(file_path, algorithm)

if calculated_hash:
    print(f"\nCalculated {algorithm.upper()} Hash: {calculated_hash}")

    if calculated_hash == known_hash:
        print("⚠ WARNING: File matches known malicious hash!")
    else:
        print("✅ File hash does NOT match the malicious hash.")
