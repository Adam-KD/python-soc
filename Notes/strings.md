# Strings

Text data. In SOC scripts almost everything starts as a string — log lines, IPs, timestamps.

## Syntax

```python
my_string = "192.168.0.1 / FAILED"
```

## Useful methods

```python
line.split(" / ")      # splits into a list — ["192.168.0.1", "FAILED"]
line.strip()           # removes whitespace and newlines from both ends
line.upper()           # "192.168.0.1 / FAILED" → "192.168.0.1 / FAILED"
line.lower()           # useful for case-insensitive comparisons
"FAILED" in line       # True/False — checks if substring exists
line.startswith("192") # True/False
line.replace("FAILED", "BLOCKED")
```

## Indexing

```python
line[0]      # first character
line[0:7]    # characters 0 to 6 (slice)
```

## f-strings — clean way to build output

```python
ip = "192.168.0.1"
count = 3
print(f"{ip} failed {count} times")
# 192.168.0.1 failed 3 times
```

## When to use

Every log line is a string. You will split, strip, and search strings in every single SOC script you write.