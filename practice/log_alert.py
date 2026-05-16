# Still Under Development

import re

logs = [
    "Jan 15 03:22:11 server sshd: Failed password for root from 192.168.0.1 port 22",
    "Jan 15 03:22:15 server sshd: Failed password for admin from 192.168.0.2 port 22",
    "Jan 15 03:22:18 server sshd: Accepted password for alice from 192.168.0.1 port 22",
    "Jan 15 03:22:21 server sshd: Failed password for root from 192.168.0.1 port 22",
    "Jan 15 03:22:25 server sshd: Failed password for guest from 192.168.0.3 port 22",
]

login_count = {}

for log in logs:
    if "Failed" in log:
        ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", log).group()
        if (ip in login_count):
                login_count[ip] += 1
        else:
                login_count[ip] = 1

for ip in login_count:
    if login_count[ip] >= 2:
        print(f"ALERT: {ip} has appeared {login_count[ip]} times.")