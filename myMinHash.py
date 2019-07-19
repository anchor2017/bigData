#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 17:05:13 2019

@author: anchor
"""

# load text
file1 = open("amazon-titles.txt", "r")
text1 = file1.read()
file1.close()
file2 = open("google-names.txt", "r")
text2 = file2.read()
file2.close()

# split into words by white space
words1 = text1.split()
words2 = text2.split()

# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped1 = [w.translate(table) for w in words1]
stripped2 = [w.translate(table) for w in words2]

from datasketch import MinHash 

# minhash
m1, m2 = MinHash(), MinHash()
for d in stripped1:
    m1.update(d.encode('utf8'))
for d in stripped2:
    m2.update(d.encode('utf8'))
print("Estimated Jaccard for data1 and data2 is", m1.jaccard(m2))

# jaccard
s1 = set(stripped1)
s2 = set(stripped2)
actual_jaccard = float(len(s1.intersection(s2)))/float(len(s1.union(s2)))
print("Actual Jaccard for data1 and data2 is", actual_jaccard)
