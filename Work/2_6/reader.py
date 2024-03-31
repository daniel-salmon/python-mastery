# reader.py

import csv
import sys

from collections import abc

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

def read_csv_as_columns(filename, types, use_intern=False):
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        dc = DataCollection(headers, types, use_intern)
        for row in rows:
            dc.append(row)
    return dc


class DataCollection(abc.Sequence):

    def __init__(self, headers, types, use_intern=False):
        if len(headers) != len(types):
            raise ValueError('headers and types must have the same length')
        self.headers = headers
        if use_intern:
            self.types = [t if t is not str else sys.intern for t in types]
        else:
            self.types = types
        self.collection = [[] for _ in headers]

    def __len__(self):
        return len(self.collection[0])

    def __getitem__(self, idx):
        if isinstance(idx, int):
            return {header: self.collection[i][idx] for i, header in enumerate(self.headers)}
        dc = DataCollection(self.headers, self.types)
        for i, _ in enumerate(dc.headers):
            dc.collection[i] = self.collection[i][idx]
        return dc

    def append(self, item):
        if isinstance(item, dict):
            for i, header in enumerate(self.headers):
                self.collection[i].append(self.types[i](item[header]))
        elif isinstance(item, list):
            for i, header in enumerate(self.headers):
                self.collection[i].append(self.types[i](item[i]))
