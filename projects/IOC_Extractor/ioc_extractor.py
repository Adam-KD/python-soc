import re
import argparse

# ── CLI setup ──────────────────────────────────────────────────────────────────
parser = argparse.ArgumentParser(description="Extract IOCs from a threat report")
parser.add_argument("--file", required=True, help="Path to the report file")
parser.add_argument("--out", choices=["json", "csv"], help="Output format (json or csv)")
args = parser.parse_args()

# ── Read report file ───────────────────────────────────────────────────────────
with open(args.file, "r") as f:
    report = f.read()

# ── Extract IOCs using regex ───────────────────────────────────────────────────

# IP addresses
ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', report)
unique_ips = set(ips)

# Domains — negative lookbehind (?<!@) prevents matching inside email addresses
domains = re.findall(r'(?<!@)\b([a-zA-Z0-9.-]+\.(?:com|net|org|io|gov|edu))\b', report)
unique_domains = set(domains)

# Email addresses
emails = re.findall(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', report)
unique_emails = set(emails)

# MD5 hashes — exactly 32 hex characters
md5_hashes = re.findall(r'\b[a-fA-F0-9]{32}\b', report)
unique_md5_hashes = set(md5_hashes)

# SHA256 hashes — exactly 64 hex characters
sha256_hashes = re.findall(r'\b[a-fA-F0-9]{64}\b', report)
unique_sha256_hashes = set(sha256_hashes)

# CVE IDs — format CVE-YYYY-NNNNN
cves = re.findall(r'CVE-\d{4}-\d{4,7}', report)
unique_cves = set(cves)

# ── Collect results into a dict ────────────────────────────────────────────────
# Sets converted to lists for JSON/CSV serialization
results = {
    "IPs": list(unique_ips),
    "Domains": list(unique_domains),
    "Emails": list(unique_emails),
    "MD5 Hashes": list(unique_md5_hashes),
    "SHA256 Hashes": list(unique_sha256_hashes),
    "CVEs": list(unique_cves),
}

# ── Output ─────────────────────────────────────────────────────────────────────

if args.out == "json":
    import json
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("Saved to results.json")

elif args.out == "csv":
    import csv
    with open("results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Type", "Value"])          # header row
        for ioc_type, values in results.items():
            for value in values:
                writer.writerow([ioc_type, value])  # one row per IOC
    print("Saved to results.csv")

else:
    # default — print to terminal
    for ioc_type, values in results.items():
        print(f"\nExtracted {ioc_type}:")
        for value in values:
            print(f"  {value}")
    total = sum(len(v) for v in results.values())
    print(f"\nTotal IOCs: {total}")