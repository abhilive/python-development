"""
Problem Statement:

You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings S of that contains 2 or more vowels.
Also, these substrings must lie in between 2 consonants and should contain vowels only.

Source: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
"""

import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags = re.I)
print('\n'.join(m or ['-1']))
