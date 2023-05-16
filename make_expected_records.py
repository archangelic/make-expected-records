#!/usr/bin/env python3
import json
import sys

# This script takes the output from `python main.py read ...` and puts into the format expected by expected_records.jsonl

# give the output of the main.py read, and the filename you want to output to
filename = sys.argv[1]
out_filename = sys.argv[2]

# read the input
with open(filename) as r:
    raw_records = r.readlines()

# sort out only the records
parsed_records = []
stream_records = []
for r in raw_records:
    line = json.loads(r.strip())
    if line['type'] == 'RECORD':
        parsed_records.append(json.dumps(line['record']))

# get a set of stream names from the records
streams = set()
for s in parsed_records:
    streams.add(json.loads(s)['stream'])

# select up to 3 records as examples
for s in streams:
    stream = [x for x in parsed_records if json.loads(x)['stream'] == s]
    stream = stream[:3]
    for x in stream:
        stream_records.append(x)

# write to the output file
with open(out_filename, 'w') as o:
    o.write('\n'.join(stream_records))
    o.write('\n')
