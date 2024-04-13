# stock.py

import csv

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


def read_portfolio(filename):
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        next(rows)
        portfolio = []
        for row in rows:
            s = Stock(row[0], int(row[1]), float(row[2]))
            portfolio.append(s)
    return portfolio

def print_portfolio(portfolio):
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print(f"{10 * '-'} {10 * '-'} {10 * '-'}")
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
