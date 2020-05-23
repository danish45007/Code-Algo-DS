"""LIFO (Last in First out)
    Methods:
    -> Push
    -> PoP
    -> Peek
    -> Size
    -> IsEmpty
"""

class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, item):
        """Push the Element at the last
            :return : None
        """
        self.items.append(item)
    
    def pop(self):
        """Pop the last element 
            :return: Last element for each call
        """
        self.items.pop()
    
    def peek(self):
        """return: the last element for each stack
        """
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return "Stack is Empty"
    
    def size(self):
        """Gives the size of the stack(no. of elements)
            :return : int
        """
        if len(self.items) > 0:
            return(len(self.items))
    
    def isEmpty(self):
        """Give the info is Stack empty or not
            :return: True or Flase
        """
        if len(self.isEmpty) > 0:
            return True
        else:
            return False
    def Print(self):
        return self.items

if __name__ == "__main__":
    s = Stack()
    s.push("1")
    s.push("2")
    s.push("3")
    print(s.size())
    s.pop()
    print(s.size())
    print(s.Print())
