#! /usr/bin/env python3
"""This is the mapper file for question 3/4"""

import sys

previous_pattern = ""
previous_pattern_count =0
current_pattern =""

"""Reading stdin as input comes from standard input"""
for line in sys.stdin:
    """Remove leading and trailing whitespace"""
    line = line.strip()

    current_pattern,_ = line.split('\t',1)

    if previous_pattern == current_pattern:
        previous_pattern_count += 1
    else:
        if previous_pattern:
            print(previous_pattern,'\t',previous_pattern_count)
        previous_pattern_count = 1
        previous_pattern = current_pattern

print(previous_pattern,'\t',previous_pattern_count)