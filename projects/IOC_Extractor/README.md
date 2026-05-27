# IOC Extractor

A command line tool that extracts Indicators of Compromise (IOCs) from threat reports and text files.

## What it extracts

- IP addresses
- Domains
- Email addresses
- MD5 hashes
- SHA256 hashes
- CVE IDs

## Requirements

Python 3.x — no external libraries needed.

## Usage

```bash
# Print to terminal
python ioc_extractor.py --file report.txt

# Save as JSON
python ioc_extractor.py --file report.txt --out json

# Save as CSV
python ioc_extractor.py --file report.txt --out csv
```

## Sample output
Extracted IPs:
192.168.1.105

Extracted Domains:
malware.evil.com
c2.badactor.net

Extracted Emails:
attacker@evil.com

Extracted MD5 Hashes:
d41d8cd98f00b204e9800998ecf8427e

Extracted SHA256 Hashes:
3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c

Extracted CVEs:
CVE-2024-1234

Total IOCs: 6

## Input format

Any plain text file — threat intelligence reports, emails, paste dumps, security advisories.

## Output files

- `results.json` — structured JSON, feeds into other tools and pipelines
- `results.csv` — opens in Excel, imports into any SIEM

## Planned
- API enrichment (AbuseIPDB, VirusTotal) for reputation scoring
- SHA1 hash extraction
- URL extraction
- Defanging support (e.g. `1.1.1[.]1` → `1.1.1.1`)
