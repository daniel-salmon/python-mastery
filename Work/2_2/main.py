import csv
from collections import defaultdict

def main():
    rides = read_rides_as_dicts('../../Data/ctabus.csv')
    drides = defaultdict(dict)
    for ride in rides:
        drides[ride['route']][ride['date']] = ride

    print('Q: How many bus routes exist in Chicago?')
    print(f'A: There are {len(drides.keys())} bus routes in Chicago')

    print('Q: How many people rode the number 22 bus on February 2, 2011?')
    print(f"A: {drides['22']['02/02/2011']['rides']} rode the 22 bus on February 2, 2011")

    ydrides = defaultdict(dict)
    for route, dride in drides.items():
        for date, ride in dride.items():
            year = date.split('/')[2]
            if year not in ydrides[route]:
                ydrides[route][year] = ride['rides']
            else:
                ydrides[route][year] += ride['rides']

    total_by_bus_route = defaultdict(int)
    for route, ydride in ydrides.items():
        for year, rides in ydride.items():
            total_by_bus_route[route] += rides

    print('Q: What is the total number of rides taken on each bus route?')
    print('A:\nroute: rides')
    items = sorted([x for x in total_by_bus_route.items()], key=lambda x: x[0])
    for route, rides in items:
        print(f'{route}: {rides}')

    print('Q: What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?')




def read_rides_as_dicts(filename):
    with open(filename, 'r') as file:
        data = []
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            data.append({
                'route': row[0],
                'date': row[1],
                'daytype': row[2],
                'rides': int(row[3]),
            })
        return data



if __name__ == '__main__':
    main()
