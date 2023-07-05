# make-expected-records
Takes output of `python main.py read ...` and makes an `expected_records.jsonl` for airbyte connectors

Requires click (`pip install click`)

The usage instructions can be found using `--help`.
```
Usage: make_expected_records.py [OPTIONS] RECORDS

Options:
  -s, --streams TEXT    Comma separated list of streams
  -n, --number INTEGER  Number of records per stream  [default: 3]
  -a, --all             Output all records for streams
  --help                Show this message and exit.
```

Example usage:
```
$ python main.py read --config secrets/config.json --catalog integration_tests/configured_catalog.json > expected_records.txt
$ /path/to/make_expected_records.py expected_records.txt > expected_records.jsonl
```
