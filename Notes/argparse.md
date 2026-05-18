# Argparse

Built-in Python library for building CLI tools.
Lets users pass arguments to your script from the terminal.

## Import

```python
import argparse
```

## Basic setup

```python
parser = argparse.ArgumentParser(description="Your script description")
parser.add_argument("--file", required=True, help="Path to the report file")
parser.add_argument("--out", choices=["json", "csv"], help="Output format")
args = parser.parse_args()
```

## Accessing arguments

```python
args.file   # whatever the user passed after --file
args.out    # whatever the user passed after --out
```

## Flags

```python
required=True             # script won't run without this flag
choices=["json", "csv"]   # restricts input to these values only
help="..."                # description shown in --help
```

## --help is automatic

```python
python ioc_extractor.py --help
```

argparse generates this for free based on your arguments.

## SOC example

```python
parser.add_argument("--file", required=True, help="Path to the report file")
parser.add_argument("--out", choices=["json", "csv"], help="Output format")
args = parser.parse_args()

with open(args.file, "r") as f:
    report = f.read()
```

## When to use

Use argparse whenever your script needs to accept input from the terminal.
It turns a script into a proper tool anyone can download and run.