logs = [
    "192.168.0.1 / FAILED",
    "192.168.0.2 / FAILED",
    "192.168.0.1 / FAILED",
    "192.168.0.1 / SUCCESS",
    "192.168.0.2 / SUCCESS",
]

fail_counts = {}

for log in logs:
    if "FAILED" in log:
        ip = log.split(" / ")[0]
        if ip in fail_counts:
            fail_counts[ip] += 1
        else:
            fail_counts[ip] = 1

for ip, count in fail_counts.items():
    print(f"{ip} failed {count} times")