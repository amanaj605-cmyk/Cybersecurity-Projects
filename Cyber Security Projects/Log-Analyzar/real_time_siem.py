import time
from collections import defaultdict

print("=== REAL-TIME SIEM ===")
print("Monitoring logs...\n")

last_size = 0
user_failures = defaultdict(int)

while True:
    try:
        with open("log.txt", "r") as file:
            logs = file.readlines()

        current_size = len(logs)

        if current_size > last_size:
            new_logs = logs[last_size:]

            for log in new_logs:
                log = log.strip()

                print("New Log:", log)

                if "LOGIN_FAILED" in log:

                    user = log.split("user=")[1]

                    user_failures[user] += 1

                    print(
                        f"⚠️ Failed login detected for {user}"
                    )

                    if user_failures[user] >= 3:
                        print(
                            f"🚨 BRUTE FORCE ALERT: {user} has {user_failures[user]} failed attempts!"
                        )

            last_size = current_size

        time.sleep(2)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
        break