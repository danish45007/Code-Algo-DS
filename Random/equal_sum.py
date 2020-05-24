'''
[51,71,17,42]
return 93
'''

def sumoftownum(a):
    k = {}
    for i in sorted(a, reverse=True):
        j = int(i / 10) + (i % 10)
    
        return j


a = [51,17,71,42]
print(sumoftownum(a))
