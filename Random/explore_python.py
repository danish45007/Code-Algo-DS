# import inspect
# print(inspect.getsource(list))
#
# l1 = [1,2,3]
# l2 = [4,5]
#
# print(l1+l2)

# class Person:
#     def __init__(self,name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.name}"
#
#     def __mul__(self,x):
#         if type(x) is not int:
#             raise Exception("Invalid argument, the type should be integer")
#
#         self.name = x*self.name
#
#     def __call__(self,y):
#         print(y)
#
#
# p = Person("danish")
# p(5)
# p*4
#
# print(p)


from queue import Queue
import inspect

q = Queue()
print(inspect.getsource(Queue))