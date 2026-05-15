logs = [
    "192.168.0.1 / FAILED",
    "192.168.0.2 / FAILED",
    "192.168.0.1 / FAILED",
    "192.168.0.1 / SUCCESS",
    "192.168.0.2 / SUCCESS",
]

fail_count = {}

for log in logs:
    ip = log.split(" / ")[0]
    if "FAILED" in log:
        if ip in fail_count:
            fail_count[ip] += 1
        else:
            fail_count[ip] = 1

for ip in fail_count:
    if fail_count[ip] >= 2:
        print("Alert: " + ip)
