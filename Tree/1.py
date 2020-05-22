class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    



class BinaryTree(object):

    def __init__(self,root):
        self.root = Node(root)
    
    def pre_order(self, start, traversal):
        '''
        Root -> Left -> Right
        '''
        if start:
            traversal += (str(start.value) + "-" )
            traversal = self.pre_order(start.left, traversal)
            traversal = self.pre_order(start.right, traversal)
        return traversal
    
    def post_order(self,start,traversal):
        '''
        Left -> Right -> Root
        '''
        if start:
            traversal = self.post_order(start.left, traversal)
            traversal += (str(start.left.value) + '-')
            traversal = self.post_order(start.right, traversal)
        return traversal


    
    
    
    
    
    
    
    
    
    
    
    
    def printTree(self, traversal_type):
        if traversal_type == "preorder":
            return self.pre_order(tree.root, "")
        if traversal_type == "postorder":
            return self.post_order(tree.root, "")






tree  = BinaryTree(1)

tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# print(tree.printTree("preorder"))

print(tree.printTree("postorder"))



# 1-2-4-5-3-6-7-