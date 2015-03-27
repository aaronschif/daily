#!/usr/bin/env python3

INF = float('Inf')
AUTHOR = "Erdös, P."
INPUT = """
7 4
Thomassen, C., Erdös, P., Alavi, Y., Malde, P. J., & Schwenk, A. J. (1989). Tight bounds on the chromatic sum of a connected graph. Journal of Graph Theory, 13(3), 353-357.
Burr, S., Erdös, P., Faudree, R. J., Rousseau, C. C., & Schelp, R. H. (1988). Some complete bipartite graph—tree Ramsey numbers. Annals of Discrete Mathematics, 41, 79-89.
Burris, A. C., & Schelp, R. H. (1997). Vertex-distinguishing proper edge-colorings. Journal of graph theory, 26(2), 73-82.
Balister, P. N., Gyo˝ ri, E., Lehel, J., & Schelp, R. H. (2007). Adjacent vertex distinguishing edge-colorings. SIAM Journal on Discrete Mathematics, 21(1), 237-250.
Erdös, P., & Tenenbaum, G. (1989). Sur les fonctions arithmétiques liées aux diviseurs consécutifs. Journal of Number Theory, 31(3), 285-311.
Hildebrand, A., & Tenenbaum, G. (1993). Integers without large prime factors. Journal de théorie des nombres de Bordeaux, 5(2), 411-484.
Balister, P. N., Riordan, O. M., & Schelp, R. H. (2003). Vertex‐distinguishing edge colorings of graphs. Journal of graph theory, 42(2), 95-109.
Schelp, R. H.
Burris, A. C.
Riordan, O. M.
Balister, P. N.
"""

def parse_input(lines):
    number = None
    books = []
    authors = []
    lines = iter(lines)
    for line in lines:
        line = line.strip()
        if line:
            number = int(line.split()[0])
            break

    for _ in range(number):
        line = next(lines)
        if not line:
            break
        book_authors = set()
        line = line.split('(')[0]
        line, author = line.split('&')
        book_authors.add(author.strip())
        for p in line.split('.,')[:-1]:
            book_authors.add(p.strip()+'.')
        books.append(book_authors)

    for line in lines:
        if line:
            authors.append(line.strip())
    return authors, books


def main():
    result = {AUTHOR: 0}
    authors, books = parse_input(INPUT.split('\n'))

    for book in books:
        smallest = INF
        for name in book:
            smallest = min(result.get(name, INF), smallest)
        for name in book:
            result[name] = min(result.get(name, INF), smallest+1)

    for author in authors:
        print(author, result[author])


if __name__ == '__main__':
    main()
