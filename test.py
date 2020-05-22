# 
from collections import Counter

def sol(s1,s2):
    counts = Counter(s1)
    l = len(s1)
    for i in range(len(s2)):
        if counts[s2[i]] > 0:
            l -= 1
        counts[s2[i]] -= 1
        if l == 0:
            return True
        start = i + 1 - len(s1)
        if start >= 0:
            counts[s2[start]] += 1
            if counts[s2[start]] > 0:
                l += 1
    return False

                
                
if __name__ == "__main__":
    
    s1 ="ab"
    s2 ="eidbaooo"

    print(sol(s1,s2))