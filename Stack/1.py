# Next largest element Aka Nearest greater to the Right

# Arr = [1,3,2,4]
# o/p = [3,4,4,-1]
# Brute Force
# for i in range(len(arr)):
#   for j in range(i+1,len(arr)):
#       As we can see the jth loop is depended on the i variable
#       The rigth Apoorch is to use Stack
#           Worst Time Complex:   O(n^2)
#           while using Stack:    O(n)



# def sol(arr,n):
#     stack = []
#     res = []

#     for i in range(n-1,-1,-1):

#         if len(stack) == 0:
#             res.append(-1)
#             stack.append(arr[i])

#         elif len(stack) > 0 and stack[0] > arr[i]:
#             res.append(stack[0])
        
#         elif len(stack) > 0 and stack[0]< arr[i]:

#             while(len(stack) and stack[0] <= arr[i]):
#                 stack.pop()
            
#             if len(stack) == 0:
#                 res.append(-1)
            
#             else:
#                 res.append(stack[0])
#         stack.append(arr[i])
#     return stack


# Python program to print next greater element using stack 

# Stack Functions to be used by printNGE() 
def createStack(): 
	stack = [] 
	return stack 

def isEmpty(stack): 
	return len(stack) == 0

def push(stack, x): 
	stack.append(x) 

def pop(stack): 
	if isEmpty(stack): 
		print("Error : stack underflow") 
	else: 
		return stack.pop() 

'''prints element and NGE pair for all elements of 
arr[] '''
def printNGE(arr): 
	s = createStack() 
	element = 0
	next = 0

	# push the first element to stack 
	push(s, arr[0]) 

	# iterate for rest of the elements 
	for i in range(1, len(arr), 1): 
		next = arr[i] 

		if isEmpty(s) == False: 

			# if stack is not empty, then pop an element from stack 
			element = pop(s) 

			'''If the popped element is smaller than next, then 
				a) print the pair 
				b) keep popping while elements are smaller and 
				stack is not empty '''
			while element < next : 
				print(str(element)+ " -- " + str(next)) 
				if isEmpty(s) == True : 
					break
				element = pop(s) 

			'''If element is greater than next, then push 
			the element back '''
			if element > next: 
				push(s, element) 

		'''push next to stack so that we can find 
		next greater for it '''
		push(s, next) 

	'''After iterating over the loop, the remaining 
	elements in stack do not have the next greater 
	element, so print -1 for them '''

	while isEmpty(s) == False: 
			element = pop(s) 
			next = -1
			return next 

# Driver program to test above functions 
arr = [1, 3, 2, 4 ] 
printNGE(arr) 

# This code is contributed by Sunny Karira 









