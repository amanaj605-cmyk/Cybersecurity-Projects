from collections import defaultdict

failed_logins = 0
success_logins = 0
user_failures = defaultdict(int)

print("=== MINI SIEM SYSTEM ===\n")

with open("log.txt", "r") as file:
    for line in file:
        line = line.strip()

        if "LOGIN_FAILED" in line:
            failed_logins += 1

            user = line.split("user=")[1]
            user_failures[user] += 1

        elif "LOGIN_SUCCESS" in line:
            success_logins += 1

print("Security Summary")
print("----------------")
print("Successful Logins:", success_logins)
print("Failed Logins:", failed_logins)

print("\nThreat Detection")
print("----------------")

threat_found = False

for user, count in user_failures.items():
    if count >= 3:
        threat_found = True
        print(f"🚨 ALERT: Possible brute-force attack detected!")
        print(f"Target User: {user}")
        print(f"Failed Attempts: {count}\n")

if not threat_found:
    print("No threats detected.")