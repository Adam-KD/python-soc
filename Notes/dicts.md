# Dicts

A dictionary stores key-value pairs. Like a real dictionary — word is the key, definition is the value.

## Syntax

```python
my_dict = {"key": value, "key2": value2}
```

## SOC example

```python
fail_counts = {}

if ip in fail_counts:
    fail_counts[ip] += 1
else:
    fail_counts[ip] = 1
```

Key = IP address. Value = how many times it failed.

## Access a value

```python
fail_counts["192.168.0.1"]  # returns the count for that IP
```

## When to use

Use a dict when you need to label your data, not just list it.
A list stores items. A dict stores items with a name attached.

## Confused by

- Remember to initialise the key first (the `else` block) before you can increment it.