# # try:
# #     import phonenumbers
# #     # from test import number
# #     from phonenumbers import geocoder
# #     from phonenumbers import carrier
# # except Exception as e:
# #     print("Some modules are missing {}".format(e))

# # number = "7550171637"
# # number = str(number)

# # ch_number = phonenumbers.parse(number,'CH')

# # print(geocoder.description_for_number(ch_number,"en"))

# # serv_num = phonenumbers.parse(number,"RO")

# # print(carrier.name_for_number(serv_num,"en"))

# def fib(n): 
#     assert n >= 0

#     fib_1 = 0
#     fib_2 = 1
#     sum = 0

#     if n <= 0:
#         return sum
#     for _ in range(n-1):
#         sum = fib_1 + fib_2
#         fib_1 = fib_2
#         fib_2 = sum
        
#     return sum

# if __name__ == "__main__":
#     print(fib(100))


# def length_longest_path(input):
#     """
#     :type input: str
#     :rtype: int
#     """
#     curr_len, max_len = 0, 0    # running length and max length
#     stack = []    # keep track of the name length
#     for s in input.split('\n'):
#         print("---------")
#         print("<path>:", s)
#         depth = s.count('\t')    # the depth of current dir or file
#         print("depth: ", depth)
#         print("stack: ", stack)
#         print("curlen: ", curr_len)
#         while len(stack) > depth:    # go back to the correct depth
#             curr_len -= stack.pop()
#         stack.append(len(s.strip('\t'))+1)   # 1 is the length of '/'
#         curr_len += stack[-1]    # increase current length
#         print("stack: ", stack)
#         print("curlen: ", curr_len)
#         if '.' in s:    # update maxlen only when it is a file
#             max_len = max(max_len, curr_len-1)    # -1 is to minus one '/'
#     return max_len

# st= "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdirectory1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
# st2 = "a\n\tb1\n\t\tf1.txt\n\taaaaa\n\t\tf2.txt"
# print("path:", st2)

# print("answer:", length_longest_path(st2))


# Python code to convert a sorted array 
# to a balanced Binary Search Tree 

# binary tree node 
class Node: 
	def __init__(self, d): 
		self.data = d 
		self.left = None
		self.right = None

# function to convert sorted array to a 
# balanced BST 
# input : sorted array of integers 
# output: root node of balanced BST 
def sortedArrayToBST(arr): 
	
	if not arr: 
		return None

	# find middle 
	mid = (len(arr)) / 2
	
	# make the middle element the root 
	root = Node(arr[mid]) 
	
	# left subtree of root has all 
	# values <arr[mid] 
	root.left = sortedArrayToBST(arr[:mid]) 
	
	# right subtree of root has all 
	# values >arr[mid] 
	root.right = sortedArrayToBST(arr[mid+1:]) 
	return root 

# A utility function to print the preorder 
# traversal of the BST 
def preOrder(node): 
	if not node: 
		return
	
	print(node.data) 
	preOrder(node.left) 
	preOrder(node.right) 

# driver program to test above function 
""" 
Constructed balanced BST is 
	4 
/ \ 
2 6 
/ \ / \ 
1 3 5 7 
"""

arr = [1, 2, 3, 4, 5, 6, 7] 
root = sortedArrayToBST(arr) 
print("PreOrder Traversal of constructed BST ")
preOrder(root) 

# This code is contributed by Ishita Tripathi 
 