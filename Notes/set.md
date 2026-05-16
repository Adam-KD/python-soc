# Sets

A set stores unique values only — duplicates are automatically removed.
In SOC scripts: deduplicating IPs, domains, or any list of IOCs.

## Syntax

```python
my_set = {1, 2, 3}

# or convert a list to a set
my_list = [1, 2, 2, 3, 3, 3]
my_set = set(my_list)
print(my_set)  # {1, 2, 3}
```

## SOC example — deduplicate extracted IPs

```python
ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", report)
unique_ips = set(ips)
```

## Difference from list

```python
my_list = [1, 2, 2, 3]   # keeps duplicates, preserves order
my_set  = {1, 2, 2, 3}   # removes duplicates, no guaranteed order
```

## When to use

Use a set when you only care about unique values and order doesn't matter.
Use a list when order matters or you need to keep duplicates.