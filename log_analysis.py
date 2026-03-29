from collections import defaultdict
import sys

THRESHOLD = 3

if len(sys.argv) <2:
    print("Usage: pyhon3 log_analysis_sys.py<logfile>")
    sys.exit(1)

filename = sys.argv[1]

counts = defaultdict(int)

with open(filename) as f:
    for line in f:
        if "failed" in line:
            ip = line.split()[0]
            counts[ip] += 1

for ip, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    if count >= THRESHOLD:
        print(f"Suspicious IP: {ip} Failed attempts: {count}")
