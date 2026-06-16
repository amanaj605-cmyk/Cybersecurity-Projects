password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1
else:
    print("Password should be at least 8 characters long")

if any(char.isupper() for char in password):
    score += 1
else:
    print("Add at least one capital letter")    

if any(char.islower() for char in password):
    score += 1
else:
    print("Add at least one lowercase letter")

if any(char.isdigit() for char in password):
    score += 1
else:
    print("Add at least one digit")

if any(not char.isalnum() for char in password):
    score += 1
else:
    print("Add at least one special character")

if score <= 2:
    print("Weak Password")
elif score <= 4:
    print("Medium Password")
else:
    print("Strong Password")