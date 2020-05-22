def Min_subset(arr,sum,n):
    
    # Creating an empty matrix
    k = [[False for x in range(sum+1)] for x in range(n+1)]
    l1 = []
    l2 = []

    for i in range(0,n+1):
        k[i][0] = True
    
    for j in range(1,sum+1):
        k[0][j] = False
    
    for i in range(n+1):
        for j in range(sum+1):
            if arr[i-1] <= j:
                k[i][j] = ((k[i-1][j]) or k[i-1][j-arr[i-1]])
            else:
                k[i][j] = k[i-1][j]

    l =  k[n-1][0:sum+1]
    for index, value in enumerate(l):
        if value == True:
            l1.append(index)
    l1 = l1[0:sum//2]
    
    for char in l1:
        l2.append(abs(sum-2*(char)))
    return min(l2)

        



if __name__ == "__main__":
    arr = [1,6,11,5]
    n = len(arr) 
    sum = sum(arr)
    print(Min_subset(arr,sum,n))