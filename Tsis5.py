import re

file = open("row.txt", "r", encoding="utf8")

text = file.read()

x=re.findall("ab*",text)
print(x)

import re

file = open("row.txt", "r", encoding="utf8")

text = file.read()

x=re.findall("a[b]{2,3}",text)
print(x)

import re

file = open("row.txt", "r", encoding="utf8")

text = file.read()

x=re.findall("[a-z]+_[a-z]+",text)
print(x)

import re

file = open("row.txt", "r", encoding="utf8")

text = file.read()

x=re.findall("[A-Z][a-z]+",text)
print(x)

import re

file = open("row.txt", "r", encoding="utf8")

text = file.read()

x=re.findall("a.*b",text)
print(x)

import re

file = open("row.txt", "r", encoding="utf8")

text = file.read()

x=re.sub("[, .]",":",text)
print(x)

import re

file = open("row.txt", "r", encoding="utf8")

text = file.read()

x=re.split("[A-Z]",text)
print(x)

import re

file = open("row.txt", "r", encoding="utf8")

text = file.read()

x=re.split("r'([a-z])([A-Z])', r'\1 \2'",text)
print(x)

import re

file = open("row.txt", "r", encoding="utf8")

text = file.read()

x=re.split("r'([a-z0-9])([A-Z])', r'\1_\2'",text)
print(x)
