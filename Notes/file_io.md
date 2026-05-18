# File I/O

Reading from and writing to files.
In SOC scripts: reading log files, report files, writing results.

## Opening a file

```python
with open("report.txt", "r") as f:
    content = f.read()
```

## Modes

```python
"r"   # read — file must exist
"w"   # write — creates file if it doesn't exist, overwrites if it does
"a"   # append — adds to existing file without overwriting
```

## `with` keyword

Automatically closes the file when the block finishes.
Without it you'd have to manually call `f.close()`.

## `f` variable

Just a convention for "file" — could be named anything.
Represents the opened file inside the `with` block.

## Reading

```python
f.read()        # reads entire file as one string
f.readlines()   # reads file as a list of lines
```

## Writing

```python
with open("results.txt", "w") as f:
    f.write("some text")
```

## SOC example — read a threat report

```python
with open(args.file, "r") as f:
    report = f.read()
```

## When to use

Use file I/O whenever your script reads from or writes to a file.
In SOC scripts: reading log files, threat reports, writing JSON or CSV results.