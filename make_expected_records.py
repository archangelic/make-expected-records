#!/usr/bin/env python3
import json

import click

# This script takes the output from `python main.py read ...` and puts into the format expected by expected_records.jsonl

def split_streams(ctx, param, value):
    try:
        return [s.strip() for s in value.split(',') if s]
    except AttributeError:
        return []

@click.command()
@click.argument('records', type=click.File('rb'))
@click.option('--streams', '-s', callback=split_streams, help="Comma separated list of streams.")
@click.option('--number', '-n', type=int, default=3, show_default=True, help="Number of records per stream.")
@click.option('--all', '-a', '_all',  is_flag=True, help='Output all records for streams.')
def parse_records(records, streams, number, _all):
    raw_records = records.readlines()

    # sort out only the records
    parsed_records = []
    stream_records = []
    for r in raw_records:
        line = json.loads(r.strip())
        if line['type'] == 'RECORD':
            parsed_records.append(line['record'])

    # get a set of stream names from output, only use specified streams
    streams_found = set()
    for r in parsed_records:
        stream_name = r['stream']
        if stream_name in streams or not streams: # use all streams if there are none specified
            streams_found.add(stream_name)

    # select records as examples
    for s in streams_found:
        stream = [x for x in parsed_records if x['stream'] == s]
        if not _all:
            stream = stream[:number]
        for x in stream:
            stream_records.append(x)

    # print the output
    for r in stream_records:
        print(r)

if __name__ == '__main__':
    parse_records()
