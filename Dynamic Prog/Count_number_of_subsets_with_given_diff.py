def Count_sub_diff(arr,diff,sum,n):

    k = [[0 for x in range(sum+1)] for x in range(n+1)]

    for i in range(n+1):
        k[i][0] = 1
    
    for j in range(1,sum+1):
        k[0][j] = 0

    for i in range(n+1):
        for j in range(sum+1):

            if (arr[i-1] <= j):
                k[i][j] = ((k[i-1][j]) + k[i-1][j-arr[i-1]])
            
            else:
                k[i][j] = k[i-1][j]
    
    return k[n][sum] - 1





if __name__ == "__main__":
    arr = [1,1,2,3]
    sum = sum(arr)
    diff = 1
    sum_s1 = (diff + sum)//2
    n = len(arr)
    print(Count_sub_diff(arr,diff,sum_s1,n))