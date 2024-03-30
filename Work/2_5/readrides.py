# readrides.py

import collections
import collections.abc

def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    import csv
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)


def read_rides_as_dicts(filename):
    import csv
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            record = {
                'route': row[0],
                'date': row[1],
                'daytype': row[2],
                'rides': int(row[3]),
            }
            records.append(record)
    return records


class RideData(collections.abc.Sequence):
    def __init__(self):
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        if isinstance(index, int):
            return {
                'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index],
            }
        # index must be a slice
        rd = RideData()
        rd.routes = self.routes[index]
        rd.dates = self.dates[index]
        rd.daytypes = self.daytypes[index]
        rd.numrides = self.numrides[index]
        return rd


    def append(self, item):
        self.routes.append(item['route'])
        self.dates.append(item['date'])
        self.daytypes.append(item['daytype'])
        self.numrides.append(item['rides'])

    @classmethod
    def read_rides(cls, filename):
        import csv
        rd = cls()
        with open(filename) as f:
            rows = csv.reader(f)
            next(rows)
            for row in rows:
                rd.routes.append(row[0])
                rd.dates.append(row[1])
                rd.daytypes.append(row[2])
                rd.numrides.append(int(row[3]))
        return rd
