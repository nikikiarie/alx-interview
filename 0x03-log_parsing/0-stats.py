#!/usr/bin/python3
import sys
import signal

size = 0
count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
lines = 0

def show():
    print(f"File size: {size}")
    for code in sorted(count.keys()):
        if count[code] > 0:
            print(f"{code}: {count[code]}")

def stop(sig, frm):
    show()
    sys.exit(0)

signal.signal(signal.SIGINT, stop)

try:
    for i in sys.stdin:
        splits = i.split()
        if len(splits) != 9:
            continue

        try:
            code = int(splits[-2])
            size_part = int(splits[-1])
        except ValueError:
            continue

        if code in count:
            count[code] += 1
        size += size_part
        lines += 1

        if lines % 10 == 0:
            show()

except KeyboardInterrupt:
    show()
    sys.exit(0)
