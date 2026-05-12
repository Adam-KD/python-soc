# Loops

Used to iterate over a list, file, or any collection of items.

## Syntax

```python
for item in collection:
    # do something with item
```

## SOC example

```python
logs = [
    "192.168.0.1 / FAILED",
    "192.168.0.2 / FAILED",
]

for log in logs:
    if "FAILED" in log:
        print(log)
```

## The variable name is yours

`log` in `for log in logs` is just a name you choose.
Python puts the current item into it on each iteration.

```python
for banana in logs:  # works exactly the same
    print(banana)
```

## When to use

Use a loop when you need to do the same thing to every item in a collection.
In SOC scripts that means every line in a log file, every IP in a list, every alert in a dataset.

## Confused by

- The loop variable doesn't exist before the loop starts — Python creates it automatically.