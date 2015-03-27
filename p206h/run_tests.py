#!/usr/bin/env python3
from pathlib import Path
from os.path import dirname
from subprocess import PIPE, Popen

DIR = Path(dirname(__file__))

def main():
    tests = {}
    p = None
    with (DIR/'test.txt').open() as f:
        for line in f.readlines():
            if line.startswith('$ '):
                print('Test')
                p = Popen([line[2:-1]], stdin=PIPE, stdout=PIPE, stderr=PIPE)
            elif line.startswith('> '):
                p.stdin.write(line[2:].encode('utf-8'))
                p.stdin.flush()
            else:
                p.stdin.close()
                l = p.stdout.readline().decode('utf-8')
                test = line.strip()
                gotten = l.strip()

                # print("'{}' '{}'".format(test, gotten))
                assert test == gotten

if __name__ == '__main__':
    main()
