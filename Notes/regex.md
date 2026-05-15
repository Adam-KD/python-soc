# Regex

Used to find and extract patterns from strings.
In SOC scripts: extracting IPs, timestamps, usernames from raw log lines.

## Import

```python
import re
```

## Two main methods

```python
re.search(pattern, string)   # finds first match, returns match object or None
re.findall(pattern, string)  # finds all matches, returns a list
```

## Output types

```python
# re.search() returns a match object — need .group() to get the string
ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", log)
print(ip.group())   # '192.168.0.1'

# re.findall() returns a plain list of strings — ready to use directly
ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", log)
print(ips)          # ['192.168.0.1', '192.168.0.2']
```

## SOC example — extract and count IPs from failed logins

```python
import re

login_count = {}

for log in logs:
    if "Failed" in log:
        ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", log).group()
        if ip in login_count:
            login_count[ip] += 1
        else:
            login_count[ip] = 1

for ip in login_count:
    if login_count[ip] >= 2:
        print(f"ALERT: {ip} has appeared {login_count[ip]} times.")
```

## The IP pattern broken down
\d{1,3}            one to three digits
(?:.\d{1,3})      a dot followed by one to three digits
{3}                repeat that three times
\b                 word boundary — stops partial matches

## findall vs search

```python
re.search()    # use when you expect one match
re.findall()   # use when you expect multiple matches — returns a list
```

## When to use over split()

split() only works when the format is consistent.
Regex works on messy, real-world log lines where fields move around.