#!/usr/bin/env rdmd

import std.stdio;

/*
# right to left
results = []
def f(n, s, m): # n=number, s=output string, m=current power of two
    if n == 0:
        results.append(s)
        return
    if m > n:
        return
    if n % (m*2) == 0:
        f(n,     "0"+s, m*2)
        f(n-m*2, "2"+s, m*2)
    else:
        f(n-m,   "1"+s, m*2)

number = input()
f(number , "", 1)
print(results)
*/

auto a(int n, int m) {
  int[] result;

  if (n==0) {
    
  }
}

auto to_bin_array(int n) pure {
  int[] result;

  int i = 1;
  while (n > i) {
    result = n % i ~ result;
    i *= 2;
  }

  return result;
}


void main() {
  writeln(to_bin_array(18));
}
