#!/usr/bin/env python3
"""This is the mapper file for question 3/4"""

import sys

complete_DNA = ""

"""Reading the files as input comes from STDID"""

for line in sys.stdin:
    """Remove leading and trailing whitespace"""
    line = line.strip()
    if((line[0]!="<" or line[0]!=">") and (line[0] in ['a','c','g','t'] or line[0] in ['A','G','T','C'])):
        
        """append the line"""
        complete_DNA = complete_DNA+line

"""splitting into words of 9-mers"""

for i in range(len(complete_DNA)-8):
    print(complete_DNA[i:i+9], '\t', 1)