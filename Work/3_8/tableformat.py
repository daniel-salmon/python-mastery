# tableformat.py

from abc import ABC, abstractmethod


class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % header for header in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % r for r in rowdata))


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(str(r) for r in rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        head = ' '.join('<th>%s</th>' % header for header in headers)
        print(f'<tr> {head} </tr>')

    def row(self, rowdata):
        r = ' '.join('<td>%s</td>' % d for d in rowdata)
        print(f'<tr> {r} </tr>')


class UpperHeadersMixin:
    def headings(self, headers):
        headers = [header.upper() for header in headers]
        super().headings(headers)


class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)


def create_formatter(fmt='text', column_formats=None, upper_headers=False):
    classes = []
    if upper_headers:
        classes.append(UpperHeadersMixin)
    if column_formats:
        class ColumnFormatter(ColumnFormatMixin):
            formats = column_formats
        classes.append(ColumnFormatter)
    if fmt == 'text':
        classes.append(TextTableFormatter)
    elif fmt == 'csv':
        classes.append(CSVTableFormatter)
    elif fmt == 'html':
        classes.append(HTMLTableFormatter)
    else:
        raise NotImplementedError(f"No table formatter with format '{fmt}'")

    class Formatter(*classes):
        pass

    return Formatter()


def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")

    formatter.headings(fields)
    for record in records:
        rowdata = [getattr(record, field, '') for field in fields]
        formatter.row(rowdata)
