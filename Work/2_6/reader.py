# reader.py

import csv

def read_csv_as_dicts(filename, datatypes):
    data = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            data.append({
                key: func(val) for key, func, val in zip(headers, datatypes, row)
            })
    return data
