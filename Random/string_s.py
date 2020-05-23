from collections import Counter

s = "PPALLL"

d = Counter(s)

if d['A'] > 1 or d['L'] > 2:
    print('False')
else:
    print('True')