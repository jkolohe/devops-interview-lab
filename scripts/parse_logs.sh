#!/usr/bin/env bash
# Simple Bash log parser: counts status codes and top endpoints
LOG_FILE="${1:-logs/sample.log}"

if [[ ! -f "$LOG_FILE" ]]; then
  echo "Log file not found: $LOG_FILE" >&2
  exit 1
fi

echo "=== Status code counts ==="
awk '{codes[$3]++} END {for (c in codes) printf "%s %d\n", c, codes[c] | "sort"}' "$LOG_FILE"

echo ""
echo "=== Top endpoints ==="
awk '{print $5}' "$LOG_FILE" | sed 's/\?.*$//' | sort | uniq -c | sort -nr | head -10
