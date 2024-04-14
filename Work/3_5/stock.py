# stock.py

import csv

from decimal import Decimal

class Stock:

    __slots__ = ('name', '_shares', '_price')

    _types = (str, int, float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f'shares must be a {self._types[1]}')
        if value < 0:
            raise ValueError('shares must be nonnegative')
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f'price must be a {self._types[2]}')
        if value < 0:
            raise ValueError('price must be nonnegative')
        self._price = value


    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)


class DStock(Stock):

    _types = (str, int, Decimal)
