class Node(object):
    # constructor
    def __init__(self,data):
        self.data = data
        self.NextNode = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0
    
    # insert at begining
    #  O(1) Time complex
    def insert(self,data):
        self.size = self.size + 1
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
        else:
            newNode.NextNode = self.head
            self.head = newNode
    
    # O(1) Time Complex 
    def Size(self):
        return self.size


    # insert at the end
    # O(n) linear list
    def insertend(self,data):
        self.size = self.size + 1
        newNode = Node(data)
        actualnode = self.head

        while actualnode.NextNode is not None:
             actualnode = actualnode.NextNode
        
        actualnode.NextNode = newNode
    

    def traverseList(self):
        actualnode = self.head

        while actualnode is not None:
            print(actualnode.data,end="->")
            actualnode = actualnode.NextNode
    
    # O(n)
    def remove(self,data):
        if self.head is None:
            return -1
        
        self.size = self.size - 1

        currNode = self.head
        prevNode = None

        while(currNode.data != data):
            prevNode = currNode
            currNode = currNode.NextNode

        if prevNode is None:
            self.head = currNode.NextNode

        else:
            prevNode.NextNode = currNode.NextNode 
             


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(12)
    ll.insert(13)
    ll.insert(14)
    ll.insertend(20)
    ll.insert(15)
    ll.insert(16)
    ll.remove(12)
    print(ll.traverseList())
    print(ll.Size())
        
             
