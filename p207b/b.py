#!/usr/bin/env python3

from a import parse_input, INF, AUTHOR, INPUT

def _r(author, map, result, number):
    defered = []
    for a in map[author]:
        if not a in result:
            result[a] = number
            defered.append(a)
    for a in defered:
        _r(a, map, result, number+1)

def main():
    authors, books = parse_input(INPUT.split('\n'))

    co_authors = {AUTHOR: set()}

    for book in books:
        for author in book:
            co_authors.setdefault(author, set()).update(book)

    result = {}
    _r(AUTHOR, co_authors, result, 1)

    for author in authors:
        print(author, result.get(author, INF))


if __name__ == '__main__':
    main()
