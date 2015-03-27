#!/usr/bin/env rdmd

import std.stdio;
import std.array;
import std.string;

string translate(string a) {
  switch (a) {
    default: return null;
    case "A": return "T";
    case "G": return "C";
    case "T": return "A";
    case "C": return "G";
  }
}

int main() {
  auto input = chomp(readln());
  auto markers = split!(string, char)(input, ' ');

  foreach (s; markers) {
    auto t = translate(s);
    if (t is null) {
      stderr.writeln("Bad input.");
      return 1;
    }
    write(t, " ");
  }

  writeln();
  return 0;
}
