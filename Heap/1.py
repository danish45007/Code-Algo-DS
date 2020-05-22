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
    if x > top(heap) and len(heap) > 3:
        heap.append(x)
        pop(top(heap))
    
    else:
        [x] + heap

def pop(heap):
    if len(heap) == 0:
        return -1
    else:
        heap.pop()



def ksmall(arr,n):
    h = createHeap()

    for i in range(0,n):
        push(h,arr[i])
    return top(h)





if __name__ == "__main__":
    arr = [7,10,4,3,20,15]
    n = len(arr)
    print(ksmall(arr,n))

    
