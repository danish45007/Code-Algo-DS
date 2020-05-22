

def sol(arr,n):

    if sum(arr) % 2 == 1:
        return False

    else:
        sum_new = sum(arr)//2
        
        k = [[False for x in range(sum_new+1)] for x in range(n+1)]

        for x in range(n+1):
            k[x][0] = True
        
        for x in range(1,sum_new+1):
            k[0][x] = False
        
        for i in range(n+1):
            for j in range(sum_new+1):
                if arr[i-1] <= j:
                    k[i][j] = ((k[i-1][j]) or k[i-1][j-arr[i-1]])
                else:
                    k[i][j] = (k[i-1][j])
        
        return k[n][sum_new]

if __name__ == "__main__":
    arr = [1,1,1,1]
    n = len(arr)
    print(sol(arr,n))