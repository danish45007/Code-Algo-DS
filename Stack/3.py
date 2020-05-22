def sol(arr,n):
    stack = []
    res = []

    for i in range(n-1,-1,-1):

        if len(stack) == 0:
            res.append(-1)
            stack.append(arr[i])

        elif len(stack) > 0 and stack[0] > arr[i]:
            res.append(stack[0])
        
        elif len(stack) > 0 and stack[0]< arr[i]:

            while(len(stack) and stack[0] > arr[i]):
                stack.pop()
            
            if len(stack) == 0:
                res.append(-1)
            
            else:
                res.append(stack[0])
        stack.append(arr[i])
    return res[::-1]

arr = [1,3,2,4]
n = len(arr)
print(sol(arr,n))


