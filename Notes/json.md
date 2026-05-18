# JSON

Built-in Python library for reading and writing JSON data.
In SOC scripts: saving results, consuming API responses, SIEM exports.

## Import

```python
import json
```

## Two main methods

```python
json.dump()    # write a dict to a JSON file
json.dumps()   # convert a dict to a JSON string
json.load()    # read a JSON file into a dict
json.loads()   # convert a JSON string into a dict
```

## Writing to a file

```python
results = {"IPs": ["192.168.1.105"], "CVEs": ["CVE-2024-1234"]}

with open("results.json", "w") as f:
    json.dump(results, f, indent=2)
```

`indent=2` makes the output human-readable with proper indentation.
Without it everything lands on one ugly line.

## Reading from a file

```python
with open("results.json", "r") as f:
    data = json.load(f)

print(data["IPs"])   # ['192.168.1.105']
```

## String conversion

```python
raw = '{"ip": "1.2.3.4", "score": 87}'
data = json.loads(raw)   # string → dict
print(data["ip"])        # '1.2.3.4'
```

## Sets must be converted to lists first

```python
json.dump({"IPs": set(["192.168.1.105"])})   # error — sets not serializable
json.dump({"IPs": list(set(["192.168.1.105"]))})   # works
```

## When to use

Use json.dump to save structured results to a file.
Use json.loads when consuming API responses from threat intel platforms.