# tableformat.py


class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()


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


def create_formatter(fmt='text'):
    if fmt == 'text':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise NotImplementedError(f"No table formatter with format '{fmt}'")


def print_table(records, fields, formatter):
    formatter.headings(fields)
    for record in records:
        rowdata = [getattr(record, field, '') for field in fields]
        formatter.row(rowdata)
