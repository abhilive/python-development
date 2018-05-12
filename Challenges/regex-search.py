"""
Problem Statement:

You are given a string S. Your task is to find the first occurrence of an alphanumeric character in S(read from left to right) that has consecutive repetitions.

Source: https://www.hackerrank.com/challenges/re-group-groups/problem
"""

import re

m = re.search(r'([a-zA-Z\d])\1', input())

print(m.group(1) if m else -1)
