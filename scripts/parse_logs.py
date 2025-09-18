#!/usr/bin/env python3
import re
import sys
from collections import Counter

log_file = sys.argv[1] if len(sys.argv) > 1 else "logs/sample.log"
pattern = re.compile(r"""
    ^(?P<ts>\S+)\s+
    (?P<level>INFO|WARN|ERROR)\s+
    (?P<status>\d{3})\s+
    (?P<method>GET|POST|PUT|DELETE|PATCH)\s+
    (?P<path>\S+)
""", re.VERBOSE)

status_counts = Counter()
endpoint_counts = Counter()
errors = 0

with open(log_file, "r") as f:
    for line in f:
        m = pattern.match(line.strip())
        if not m: 
            continue
        status = m.group("status")
        path = m.group("path").split('?')[0]
        status_counts[status] += 1
        endpoint_counts[path] += 1
        if status.startswith("5"):
            errors += 1

print("=== Status code counts ===")
for code, count in sorted(status_counts.items()):
    print(f"{code} {count}")

print("\n=== Top endpoints ===")
for path, count in endpoint_counts.most_common(10):
    print(f"{count} {path}")

print(f"\nTotal 5xx errors: {errors}")
