'''
Maximum area under binary rectangle
STACK
NSL
NSR
MAH
2D to 1D
pass all the 1D to MAH and return max(MAH(1D))
'''

# Step-1
# Creating the Stack
def createStack():
    stack = []
    return stack

# Check if the given stack is empty or not

def isempty(stack):
    return len(stack) == 0

# Adding element to the stack
def push(stack,x):
    stack.append(x)

# Removing the element from the satck

def pop(stack):
    if isempty(stack):
        return "Error: Stack underflow"
    else:
        stack.pop()

# returning the top element of the stack

def top(stack):
    if isempty(stack):
        return "Error: stack underflow"
    else:
        return stack[len(stack)-1]

# Step-2
# NSL(Nearest smallest to left)

def NSL(arr,n):
    s = createStack()
    res = []
    o = []
    

    for i in range(0,n):

        # If stack empty and the First ele

        if isempty(s) and arr[i] == arr[0]:
            push(res,-1)
            push(s,arr[i])
        
        # If len(stack) > 0 and top(s) < arr[i]
            # return top(s) to res
        
        elif isempty(s) == False and top(s) < arr[i]:
            push(res,top(s))
        
        elif isempty(s) == False and top(s) > arr[i]:
            while(len(s) > 0 and top(s) > arr[i]):
                pop(s)
            
            if isempty(s):
                push(res,-1)
            else:
                push(res,top(s))
        
        push(s,arr[i])

        if res[i] == -1:
            o.append(-1)
        else:
            o.append(arr.index(res[i]))
    return o
        

def NSR(arr,n):
    s = createStack()
    res = []
    o = []

    for i in range(n-1,-1,-1):

        # If stack empty and the First ele

        if isempty(s) and arr[i] == arr[n-1]:
            push(res,-1)
            push(s,arr[i])
        
        # If len(stack) > 0 and top(s) < arr[i]
            # return top(s) to res
        
        elif isempty(s) == False and top(s) < arr[i]:
            push(res,top(s))
        
        elif isempty(s) == False and top(s) > arr[i]:
            while(len(s) > 0 and top(s) > arr[i]):
                pop(s)
            
            if isempty(s):
                push(res,-1)
            else:
                push(res,top(s))
        
        push(s,arr[i])
        r = res[::-1]

        
    for i in range(len(r)):    
        if r[i] == -1:
            o.append(len(r))
        else:
            o.append(arr.index(r[i]))
    return o

def area(index_nsl,index_nsr):
    width = []
    area = []
    for i in range(len(index_nsl)):
        wid = index_nsr[i] - index_nsl[i] - 1
        width.append(wid)
        area.append(arr[i]*width[i])
    return max(area)



def two_to_1D(arr):
    d = []
    for j in range(len(arr)):
        d.append(arr[0][j])

    for i in range(1,len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 0:
                d[j]= 0
            else:
                d[j] = d[j] + arr[i][j]
    
    return d

    
    
# Driver Code
if __name__ == "__main__":
    arr = [[0,1,1,0]]
    n = len(arr)
    index_nsl = (NSL(arr,n))
    index_nsr = NSR(arr,n)
    print(area(index_nsl,index_nsr))
 


