import time
from collections import defaultdict
from datetime import datetime

print("=== REAL-TIME SIEM V2 ===")
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

                    count = user_failures[user]

                    print(
                        f"⚠️ Failed login detected for {user} ({count})"
                    )

                    timestamp = datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )

                    if count == 3:

                        alert = (
                            f"\n[{timestamp}]\n"
                            f"WARNING ALERT\n"
                            f"User: {user}\n"
                            f"Failed Attempts: {count}\n"
                        )

                        print(
                            f"⚠️ WARNING: {user} has {count} failed attempts!"
                        )

                        with open("alerts.txt", "a") as f:
                            f.write(alert)

                    elif count >= 5:

                        alert = (
                            f"\n[{timestamp}]\n"
                            f"CRITICAL ALERT\n"
                            f"User: {user}\n"
                            f"Failed Attempts: {count}\n"
                        )

                        print(
                            f"🚨 CRITICAL ALERT: {user} has {count} failed attempts!"
                        )

                        with open("alerts.txt", "a") as f:
                            f.write(alert)

            last_size = current_size

        time.sleep(2)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
        break