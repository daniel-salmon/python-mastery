# main.py

import csv
from collections import namedtuple

Result = namedtuple('Result', ['result', 'current_memory_MB', 'peak_memory_MB'])

Row = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

class RowClass:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

    def __repr__(self):
        return f"RowClass({self.route!r}, {self.date!r}, {self.daytype!r}, {self.rides!r})"

class RowClassSlots:
    __slots__ = ['route', 'date', 'daytype', 'rides']

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

    def __repr__(self):
        return f"RowClassSlots({self.route!r}, {self.date!r}, {self.daytype!r}, {self.rides!r})"

def malloc(func):
    import tracemalloc

    MB = 1_000_000
    def wrapped(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return Result(result, current / MB, peak / MB)
    return wrapped

def singlestring(filename):
    with open(filename) as f:
        data = f.read()
    return data

def listofstrings(filename):
    with open(filename) as f:
        data = f.readlines()
    return data

def listoftuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = (row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

def listofdicts(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = {'route': row[0], 'date': row[1], 'daytype': row[2], 'rides': int(row[3])}
            records.append(record)
    return records

def listofnamedtuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = Row(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

def listofrowclasses(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = RowClass(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

def listofrowclassslots(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = RowClassSlots(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records


def test_funcs(funcs, reps, *args, **kwargs):
    malloced_funcs = [(func.__name__, malloc(func)) for func in funcs]
    for func_name, func in malloced_funcs:
        currents = []
        peaks = []
        for i in range(reps):
            data, current, peak = func(*args, **kwargs)
            currents.append(current)
            peaks.append(peak)
        mean_current = sum(currents) / len(currents)
        mean_peak = sum(peaks) / len(peaks)
        current = f'Current {mean_current:0.4f}MB'
        peak = f'Peak {mean_peak:0.4f}MB'
        print(f"Average memory usage of {func_name} over {reps} reps: {current}, {peak}")

def main(args):
    if len(args) == 1:
        filename = '../../Data/ctabus.csv'
    else:
        filename = args[1]

    funcs = [
        singlestring,
        listofstrings,
        listoftuples,
        listofdicts,
        listofnamedtuples,
        listofrowclasses,
        listofrowclassslots,
    ]

    test_funcs(funcs, 5, filename)

if __name__ == '__main__':
    import sys
    main(sys.argv)
