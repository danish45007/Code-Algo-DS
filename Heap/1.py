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
    heap.append(x)        

def pop(heap):
    if len(heap) == 0:
        return -1
    else:
        heap.pop()



def ksmall(arr,n,k):
    h = createHeap()

    for i in range(0,n):
        if len(h) == 0:
            push(h,arr[i])
        
        elif arr[i] > top(h):
            h.append(arr[i])
        
        else:
            [arr[i]] + h
    
    
    push(h,arr[i])
    
    return len(h)


if __name__ == "__main__":
    arr = [7,10,4,3]
    n = len(arr)
    print(ksmall(arr,n,3))

    
