'''
Heap ->
    createHeap()
    top()
    push()
    pop()
'''

# creating heap
def createHeap():
    heap = []
    return heap

# return the top element
def top(heap):
    if len(heap) == 0:
        return -1
    else:
        return heap[len(heap)-1]

# Min.heap
# push

def push(heap,x):
    if len(heap) == 0:
        heap.append(x)
    
    elif len(heap) > 0 and x < top(heap):
        heap.append(x)
    
    elif len(heap) > 0 and x > top(heap):
        heap.insert(0,x)

# pop
def pop(heap):
    if len(heap) == 0:
        return -1
    else:
        heap.pop()


# prob logic
def sort_k_sorted(arr,n,k):
    sort_list = []
    h = createHeap()
    for i in range(0,n):
        push(h,arr[i])

        if len(h) > k:
            sort_list.append(h.pop())
         

    
    return sort_list + sorted(h)    

if __name__ =="__main__":
    arr = [3,2,1,5,6,4]
    n = len(arr)
    k = 2
    print(sort_k_sorted(arr,n,k))
