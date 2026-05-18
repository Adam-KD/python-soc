# CSV

Built-in Python library for reading and writing CSV files.
In SOC scripts: saving results in a format that opens in Excel or imports into a SIEM.

## Import

```python
import csv
```

## Writing to a file

```python
with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Type", "Value"])   # header row
    writer.writerow(["IPs", "192.168.1.105"])
```

`newline=""` prevents blank lines between rows on Windows.

## writer object

`csv.writer(f)` creates a writer that formats your data with commas automatically.
`writer.writerow()` writes one row at a time — takes a list, each item becomes a column.

## Writing multiple rows from a dict

```python
for ioc_type, values in results.items():
    for value in values:
        writer.writerow([ioc_type, value])
```

## Reading from a file

```python
with open("results.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

## DictWriter — write dicts directly

```python
with open("results.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["ip", "score", "verdict"])
    writer.writeheader()
    writer.writerows(results)
```

## When to use

Use CSV when the output needs to open in Excel or import into a SIEM.
Use JSON when the output feeds into another script or API.