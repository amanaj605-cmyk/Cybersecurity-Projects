import time

print("=== REAL-TIME LOG MONITOR ===")
print("Watching log.txt for changes...\n")

last_size = 0

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
                    print("🚨 ALERT: Failed login detected!")

            last_size = current_size

        time.sleep(2)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
        break