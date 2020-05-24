from collections import Counter
import heapq
l = [4,1,-1,2,-1,2,3]
k = 2

d = Counter(l)

print(heapq.nlargest(k,d.keys(),key=d.get))
