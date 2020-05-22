'''
input: "([{}])"
output: Balanced

input: "{[()])"
output: Unbalaced

'''
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
    
    def match_symbol(symbol_str):
        symbol_str = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        openers = symbol_str.keys()
        my_stack = Stack()

        index = 0

        while(index < len(symbol_str)):
            symbol = symbol_str[index]

            if symbol in openers:
                my_stack.push(symbol)
            else:
                if my_stack.isEmpty():
                    return False
                else:
                    top_item = my_stack.pop()
                    if symbol != symbol_str[top_item]:
                        return False    

    
