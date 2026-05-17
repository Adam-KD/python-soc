import re

report = """
Malicious activity from 192.168.1.105.
C2 server at malware.evil.com and c2.badactor.net.
Hash: d41d8cd98f00b204e9800998ecf8427e
Vulnerability exploited: CVE-2024-1234
Contact: attacker@evil.com
"""

ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', report)
unique_ips = set(ips)
domains = re.findall(r'(?<!@)\b([a-zA-Z0-9.-]+\.(?:com|net|org|io|gov|edu))\b', report)
unique_domains = set(domains)
emails = re.findall(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', report)
unique_emails = set(emails)
md5_hashes = re.findall(r'\b[a-fA-F0-9]{32}\b', report)
unique_md5_hashes = set(md5_hashes)
sha256_hashes = re.findall(r'\b[a-fA-F0-9]{64}\b', report)
unique_sha256_hashes = set(sha256_hashes)
cves = re.findall(r'CVE-\d{4}-\d{4,7}', report)
unique_cves = set(cves)


print("Extracted IPs from Report: ")
for ip in unique_ips:
    print(ip)

print("\nExtracted Domains from Report: ")
for domain in unique_domains:
    print(domain)

print("\nExtracted Emails from Report: ")
for email in unique_emails:
    print(email)

print("\nExtracted MD5 Hashes from Report: ")
for md5_hash in unique_md5_hashes:
    print(md5_hash)

print("\nExtracted SHA-256 Hashes from Report: ")
for sha256_hash in unique_sha256_hashes:
    print(sha256_hash)

print("\nExtracted CVEs from Report: ")
for cve in unique_cves:
    print(cve)

print(f"\nTotal IPs: {len(unique_ips)}")
print(f"Total Domains: {len(unique_domains)}")
print(f"Total Emails: {len(unique_emails)}")
print(f"Total MD5 Hashes: {len(unique_md5_hashes)}")
print(f"Total SHA-256 Hashes: {len(unique_sha256_hashes)}")
print(f"Total CVEs: {len(unique_cves)}")