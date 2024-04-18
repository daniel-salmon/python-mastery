# stock.py

import csv
import sys
import validate

from decimal import Decimal

from validate import NonEmptyString, PositiveInteger, PositiveFloat

class Stock:

    __slots__ = ('_name', '_shares', '_price')

    _types = (str, int, float)

    _validators = (NonEmptyString, PositiveInteger, PositiveFloat)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) == (other.name, other.shares, other.price))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._validators[0].check(value)

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        self._shares = self._validators[1].check(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = self._validators[2].check(value)


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


class redirect_stdout:

    def __init__(self, out_file):
        self.out_file = out_file

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file

    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout
