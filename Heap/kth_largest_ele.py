# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         return self.ksmall(nums,n,k)
    
#     def createHeap(self):
#         heap = []
#         return heap

#     def top(self,heap):
#         if len(heap) == 0:
#             return -1
#         else:
#             return heap[len(heap)-1]

#     def push(self,heap,x):
#         if len(heap) == 0:
#             heap.append(x)
#         elif x > self.top(heap):
#             heap.append(x)
#         elif x < self.top(heap):
#             heap.insert(0,x)

#     def pop(self,heap):
#         if len(heap) == 0:
#             return -1
#         else:
#             heap.pop()


#     def ksmall(self,arr,n,k):
#         h = self.createHeap()
#         for i in range(n):
#             self.push(h,arr[i])

#             if len(h) > k:
#                 self.pop(h)

#         return self.top(h)


'''
HEAP ->
    push()
    pop()
    top()
'''
def createHeap():
    heap = []
    return heap

def top(heap):
    if len(heap) == 0:
        return -1
    else:
        return heap[len(heap)-1]

def push(heap,x):
    if len(heap) == 0:
        heap.append(x)
    elif x < top(heap):
        heap.append(x)
    elif x > top(heap):
        heap.insert(0,x)

def pop(heap):
    if len(heap) == 0:
        return -1
    else:
        heap.pop()


def ksmall(arr,n,k):
    h = createHeap()
    for i in range(n):
        push(h,arr[i])

        if len(h) > k:
            pop(h)
    
    return h[0:len(h)]


if __name__ == "__main__":
    arr = [3,2,1,5,6,4]
    n = len(arr)
    k = 2
    print(ksmall(arr,n,k))

    
