# def isSubsetSum(set,n,sum): 
      
#     # The value of subset[i][j] will be  
#     # true if there is a 
#     # subset of set[0..j-1] with sum equal to i 
#     subset=([[False for i in range(sum+1)]  
#             for i in range(n+1)]) 
      
#     # If sum is 0, then answer is true  
#     for i in range(n+1): 
#         subset[i][0] = True
          
#     # If sum is not 0 and set is empty,  
#     # then answer is false  
#     for i in range(1,sum+1): 
#          subset[0][i]=False
              
#     # Fill the subset table in botton up manner 
#     for i in range(1,n+1): 
#         for j in range(1,sum+1): 
#             if j<set[i-1]: 
#                 subset[i][j] = subset[i-1][j] 
#             if j>=set[i-1]: 
#                 subset[i][j] = (subset[i-1][j] or 
#                                 subset[i-1][j-set[i-1]]) 
      
#     # uncomment this code to print table  
#     # for i in range(n+1): 
#     #    for j in range(sum+1): 
#     #       print (subset[i][j],end=" ") 
#     #    print() 
#     return subset[n][sum] 
          
# # Driver program to test above function 
# if __name__=='__main__': 
#     set = [1,2,3,4,5,6] 
#     sum = 9
#     n =len(set) 
#     if (isSubsetSum(set, n, sum) == True): 
#         print("Found a subset with given sum") 
#     else: 
#         print("No subset with given sum") 
# /////////////////////////////////////////////////////////////////

# Code Written by @Danish45007


def subset(arr,sum,n):

    
    k = [[False for x in range(sum+1)] for x in range(n+1)]

    for i in range(0,n+1):
        k[i][0] = True
    
    for j in range(1, sum+1):
        k[0][j] = False
    
    for i in range(n+1):
        for j in range(sum+1):
            if arr[i-1] <= j:
                k[i][j] = ((k[i-1][j]) or k[i-1][j-arr[i-1]])
            else:
                k[i][j] = k[i-1][j]
    
    return k[n][sum]
    
    


if __name__ == "__main__":
    arr = [2,3,7,8,10]
    sum = 14
    n = len(arr)
    print(subset(arr,sum,n))
