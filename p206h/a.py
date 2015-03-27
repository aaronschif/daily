#!/usr/bin/env python
import sys

def op_on(oper, a, b):
    if a is None or b is None:
        return None
    if oper == '+':
        return a + b
    if oper == '-':
        return b - a
    if oper == '/':
        return b / a
    if oper == '*':
        return a * b

def value(e, l):
    if e.startswith('('):
        e = e.strip('()')
        return l.get(len(l) - int(e), None)
    else:
        return int(e)

def evaluate(expression, _list):
    values = []
    for e in expression:
        if e in '+/-*':
            values.append(op_on(e, values.pop(), values.pop()))
        else:
            v = value(e, _list)
            if v is None:
                return None
            values.append(v)
    assert len(values) == 1
    return values[0]


def read_input():
    lines = sys.stdin.readlines()
    lines = filter(lambda x: x.strip(), lines)
    assert len(lines) >= 3
    e = lines[0].strip().split(' ')
    values = {}
    for v in lines[1:-1]:
        i, n = v.strip().split(':')
        values[int(i)] = int(n)
    number = int(lines[-1])
    return e, values, number


def main():
    expression, values, number = read_input()

    for i in range(number+1):
        if values.has_key(i): continue
        values[i] = evaluate(expression, values)

    for i, v in sorted(values.items()):
        if not v is None:
            print '{}: {}'.format(i, v)


if __name__ == '__main__':
    main()
