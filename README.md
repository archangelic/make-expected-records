# make-expected-records
Takes output of `python main.py read ...` and makes an `expected_records.jsonl` for airbyte connectors

Only outputs up to 3 records per stream.

```
$ python main.py read --config secrets/config.json --catalog integration_tests/configured_catalog.json > expected_records.txt
$ /path/to/make_expected_records.py expected_records.txt expected_records.jsonl
```
