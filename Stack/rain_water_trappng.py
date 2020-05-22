

def sol(arr,n):
    l = []
    res = []
    



    for i in range(n):
        for j in range(1,n-1):
            b_left = arr[i:j]
            b_right = arr[j+1:n]
            
            b_left_max = max(b_left)
            b_right_max = max(b_right)
            l.append(b_left_max)
            l.append(b_right_max)

            min_val = min(l)

            res.append(min_val-arr[j])

        return sum(res)


            


            
            
            
    
            


arr = [3,0,0,2,0,4]
n = len(arr)
print(sol(arr,n))

