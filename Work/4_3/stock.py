# stock.py

import csv
import sys
import validate

from decimal import Decimal

from validate import String, PositiveInteger, PositiveFloat

class Stock:

    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock({self.name!r}, {self.shares!r}, {self.price!r})"

    @property
    def cost(self):
        return self.shares * self.price

    def sell(nshares):
        self.shares -= nshares
