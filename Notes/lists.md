# Lists

An ordered collection of items. Used to store multiple values in one variable.

## Syntax

```python
my_list = ["item1", "item2", "item3"]
```

## SOC example

```python
logs = [
    "192.168.0.1 / FAILED",
    "192.168.0.2 / FAILED",
    "192.168.0.1 / SUCCESS",
]
```

## Access by position

```python
logs[0]  # "192.168.0.1 / FAILED"
logs[1]  # "192.168.0.2 / FAILED"
```

Position starts at 0, not 1.

## Useful methods

```python
logs.append("192.168.0.3 / FAILED")  # add an item
len(logs)                             # how many items
"FAILED" in logs                      # check if item exists
```

## split() returns a list

```python
"192.168.0.1 / FAILED".split(" / ")  # ["192.168.0.1", "FAILED"]
```

That's why [0] gives you the IP and [1] gives you the status.

## When to use

Use a list when order matters or when you need to loop through items.
In SOC scripts: a list of log lines, a list of IPs, a list of alerts.

## Difference from dict

A list is accessed by position. A dict is accessed by a named key.