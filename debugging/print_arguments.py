#!/usr/bin/python3
import sys

args = sys.argv[1:]

if len(args) == 0:
    print("0 arguments.")
else:
    label = "argument" if len(args) == 1 else "arguments"
    print(f"{len(args)} {label}:")
    for i, a in enumerate(args, 1):
        print(f"{i}: {a}")
