

def Count_sub(arr,sum,n):

    k = [[0 for x in range(sum+1)] for x in range(n+1)]

    for i in range(0,n+1):
        k[i][0] = 1
    
    for j in range(1, sum+1):
        k[0][j] = 0
    
    for i in range(n+1):
        for j in range(sum+1):
            if arr[i-1] <= j:
                k[i][j] = ((k[i-1][j]) + k[i-1][j-arr[i-1]])
            else:
                k[i][j] = k[i-1][j]
    
    return (k[n][sum]) - 1   




if __name__ == "__main__":
    arr = [2,3,5,6,8,10]
    sum = 10
    n = len(arr)
    print(Count_sub(arr,sum,n))