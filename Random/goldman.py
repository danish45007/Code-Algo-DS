import itertools as it
def demo():
    weights = [5,7]
    measured = set()
    for factor in it.product([1,0,-1], repeat=2):
        curSum = 5* factor[0] + factor[1]
        if curSum > 0:
            measured.add(curSum)

    print(measured)

def solve():
    weights = [x for x in range(1,41)]
    all_seq = [x for x in it.combinations(weights, 4) if sum(x) is 40]
    
    for seq in all_seq:
        mes = set()
        for factor in it.product([1,0,-1], repeat=4):
            currSum = sum([seq[i] * factor[i] for i in range(4)])
            if currSum > 0:
                mes.add(currSum)

        if len(mes) is 40:
            print('Winner seq is', seq)
            break

    
