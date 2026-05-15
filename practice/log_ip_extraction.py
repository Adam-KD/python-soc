import re

log = "Failed login from 192.168.0.1 and 192.168.0.2 at 03:22:11"

ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", log)

for ip in ips:
    print(ip)