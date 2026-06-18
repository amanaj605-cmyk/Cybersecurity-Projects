from collections import defaultdict

print("Script is running...")

failed_logins = 0
success_logins = 0
user_failures = defaultdict(int)

with open("log.txt", "r") as file:
    for line in file:
        line = line.strip()

        if "LOGIN_FAILED" in line:
            failed_logins += 1
            user = line.split("user=")[1]
            user_failures[user] += 1

        elif "LOGIN_SUCCESS" in line:
            success_logins += 1

print("\n=== LOG ANALYSIS REPORT ===")
print("Successful Logins:", success_logins)
print("Failed Logins:", failed_logins)

print("\n=== Suspicious Users ===")
for user, count in user_failures.items():
    if count >= 2:
        print(user, "->", count, "failed attempts ⚠️")