'''
    Step 1: Create Stack 
    Step2: Solve Problem
'''
# Creating a Stack
def createStack():
    stack = []
    return stack

# check if stack empty
def isempty(stack):
    return len(stack) == 0

# push element into the stack

def push(stack, x):
    stack.append(x)

def pop(stack):
    if isempty(stack):
        print("Error: stack underflow")
    else:
        return stack.pop()
def top(stack):
    if isempty(stack):
        print("Error: stack underflow")
    else:
        return stack[len(stack)-1]
        
# Step: 2

def printNGE(arr,n):
    s = createStack()
    res = []
    for i in range(n-1,-1,-1):

        if isempty(s) == True and arr[i] == arr[n-1]:
            push(res,-1)
            push(s,arr[i])
        
        elif isempty(s) == False and top(s) > arr[i]:
            push(res,top(s))
        
        elif isempty(s) == False and top(s) < arr[i]:

            while (len(s) > 0 and top(s) < arr[i]):
                pop(s)
            
            if isempty(s):
                push(res,-1)
            
            else:
                push(res,top(s))
        
        push(s,arr[i])
    
    return res[::-1]


arr = [1,3,2,4]
n = len(arr)
print(printNGE(arr,n))

