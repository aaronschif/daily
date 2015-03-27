import pytest
from subprocess import Popen, PIPE
from StringIO import StringIO

TESTS = [
("""
(1) (2) +
0:0
1:1
20
""",
"""
0: 0
1: 1
2: 1
3: 2
4: 3
5: 5
6: 8
7: 13
8: 21
9: 34
10: 55
11: 89
12: 144
13: 233
14: 377
15: 610
16: 987
17: 1597
18: 2584
19: 4181
20: 6765
""")
]


@pytest.mark.parametrize('input,output', TESTS)
def test_205(input, output):
    assert output.strip() == Popen(['./a.py'], stdin=PIPE, stdout=PIPE).communicate(input.strip())[0].strip()
