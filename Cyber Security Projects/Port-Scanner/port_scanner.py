import socket
import time

target = input("Enter target IP or domain: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

start_time = time.time()

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

open_ports = []

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        open_ports.append(port)
        print(f"Port {port} is OPEN")

    s.close()

end_time = time.time()

print("\nScan Complete.")

print("\nOpen Ports:")
for port in open_ports:
    print(port)

print(f"\nTotal Open Ports: {len(open_ports)}")
print(f"Time Taken: {end_time - start_time:.2f} seconds")