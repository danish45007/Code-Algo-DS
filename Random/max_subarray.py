def circluar(l,i):
    if i > len(l)-1:
        for j in range(len(l)):
            i = i-j
    return l[i]



def Max_Sub(l):
    l1= []
    for i in range(0,len(l)):
        for j in range(len(l)):
            ll = l[i:j+1]
            if ll == []:
                pass
            else:
                l_sum = sum(ll)
                l1.append(l_sum)
                
    return max(l1)
l = [5,-3,5]
for i in range(len(l)-1):
    print(Max_Sub(circluar(l,i)))




print(circluar(l,6))  