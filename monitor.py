"""Collect monitoring settings for The Knowledge Hub."""

hostname = input("Enter the system hostname: ").strip()
ip_address = input("Enter the system IP address: ").strip()
metrics_input = input("Enter metrics separated by commas: ").strip()

metrics = []

for metric in metrics_input.split(","):
    metric = metric.strip()
    if metric:
        metrics.append(metric)

print("\nMonitoring settings")
print("-------------------")
print(f"Hostname: {hostname}")
print(f"IP address: {ip_address}")
print("Metrics:")

for metric in metrics:
    print(f"  - {metric}")