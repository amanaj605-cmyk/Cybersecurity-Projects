from collections import defaultdict

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

report = []
report.append("=== SECURITY REPORT ===")
report.append(f"Successful Logins: {success_logins}")
report.append(f"Failed Logins: {failed_logins}")
report.append("")

for user, count in user_failures.items():
    if count >= 3:
        report.append("ALERT: Possible brute-force attack detected!")
        report.append(f"Target User: {user}")
        report.append(f"Failed Attempts: {count}")

with open("security_report.txt", "w") as file:
    file.write("\n".join(report))

print("✅ Security report generated!")