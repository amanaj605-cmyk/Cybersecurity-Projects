import hashlib

filename = input("Enter file name: ")

with open(filename, "rb") as file:
    file_data = file.read()
    current_hash = hashlib.sha256(file_data).hexdigest()

hash_file = filename + ".hash"

try:
    with open(hash_file, "r") as file:
        original_hash = file.read()

    if current_hash == original_hash:
        print("File is safe.")
    else:
        print("WARNING: File has been modified!")

except FileNotFoundError:
    with open(hash_file, "w") as file:
        file.write(current_hash)

    print("Hash saved successfully.")
    print("Run the program again to verify integrity.")