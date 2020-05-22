'''
    Step 1: Create Stack
    Step 2: Solv the Problem
'''

# Step-1
# Creating a Stack
def createStack():
    stack = []
    return stack

# check if stack is empty
def isempty(stack):
    return len(stack) == 0

# Adding element into the stack
def push(stack,x):
    stack.append(x)

# Removing the element from the stack

def pop(stack):
    if isempty(stack):
        print("Error: Stack Underflow")
    else:
        return stack.pop()

# return the top element of the stack

def top(stack):
    if isempty(stack):
        print("Error: Stack underflow")
    else:
        return stack[len(stack)-1]

# Step-2
# Solving the problem

def printNGL(arr,n):
    s = createStack()
    res = []

    for i in range(0,n):

        if isempty(s) and arr[i] == arr[0]:
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
    
    return res

arr = [100,80,60,70,60,75,85]
n = len(arr)
print(printNGL(arr,n))

