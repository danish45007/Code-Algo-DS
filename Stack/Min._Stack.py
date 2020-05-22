'''
    Stack = []
    Support Stack = []
    arr = Given
'''

s = []
ss = []

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
# implement modifid push/pop/min func.

def Push(x):
    
    push(s,x)

    if isempty(ss) or top(ss) >= x:
        push(ss,x)
    


def Pop():
    
    if len(s) == 0:
        return -1
    
    ans = top(s)

    pop(s)

    if top(ss) == ans:
        pop(ss)
    
    return ans


def min():
    if len(ss) == 0:
        return -1
    else:
        return top(ss)



Push(18)
Push(19)
Push(29)
Push(15)
Push(16)
Pop()
Pop()



print(min())