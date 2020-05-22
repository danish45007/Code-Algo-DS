# Global declaration of matraix

# init matrix 102 x 1002 with -1

t = [[-1]*102 for i in range(1002)]


def  Knapsack(wt,val,W, n):

    # Base Condition
    if n == 0 or W == 0:
        return 0
    
    # Memoization saving all the new value into the matrix and if the repeated call is occuring return the output from the matrix
    if (t[n][W] != -1):
        return t[n][wt]
    

    # Choice diagram

    if (wt[n-1] <= W):
        
        t[n][W] = max((val[n-1] + Knapsack(wt,val,W-wt[n-1],n-1)),Knapsack(wt,val,W,n-1))
        return t[n][W]
    
    elif (wt[n-1] > W):
        t[n][W] = Knapsack(wt,val,W,n-1)
        return t[n][W]

if __name__ == "__main__":
    val = [60, 100, 110] 
    wt = [10, 20, 25] 
    W = 50
    n = len(val)
    print(Knapsack(wt,val,W,n))
