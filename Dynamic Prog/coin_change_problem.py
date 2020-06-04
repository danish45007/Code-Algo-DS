def coin(arr,n,sum):
    k = [[0 for x in range(sum+1)] for x in range(n+1)]
    
    # Init matrix
    for i in range(n+1):
        k[i][0] = 1


    for i in range(1,n+1):
        for j in range(1,sum+1):

            if arr[i-1] <= j:
                k[i][j] = ((k[i-1][j]) + k[i][j-arr[i-1]])

            else:
                k[i][j] = k[i-1][j]

    return k[n][sum]            



if __name__ == "__main__":
    arr = [1,2,5]
    n = len(arr)
    sum = 5
    print(coin(arr,n,sum))