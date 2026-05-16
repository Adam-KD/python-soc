import re

report = """
Threat intelligence report - January 2024.
Malicious activity detected from 192.168.1.105 targeting internal systems.
Secondary C2 communication observed from 10.0.0.23 and 185.220.101.45.
Lateral movement attempts from 192.168.1.105 to 192.168.1.200.
Known malware host: 45.33.32.156. Recommend blocking immediately.
"""

ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", report)
unique_ips = set(ips)

print("Extracted IPs from Report: \n")
for ip in unique_ips:
    print(ip)

print(f"\nTotal IPs: {len(unique_ips)}")