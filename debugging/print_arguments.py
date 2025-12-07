#!/usr/bin/python3
import sys

def main():
    args = sys.argv[1:]  # استبعد اسم السكربت (argv[0])
    if len(args) == 0:
        print("0 arguments.")
        return
    print(f"{len(args)} arguments:")
    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
