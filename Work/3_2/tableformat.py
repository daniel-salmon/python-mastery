# tableformat.py

def print_table(items, names):
    header = ' '.join('%10s' for _ in names)
    line = ' '.join(f"{10 * '-'}" for _ in names)
    print(header % tuple(names))
    print(line)
    for item in items:
        fmts = []
        vals = []
        for name in names:
            if not hasattr(item, name):
                fmts.append('%10s')
                vals.append('')
                continue
            val = getattr(item, name)
            if isinstance(val, int):
                fmts.append('%10d')
            elif isinstance(val, float):
                fmts.append('%10.2f')
            else:
                fmts.append('%10s')
            vals.append(val)
        print(' '.join(fmts) % tuple(vals))
