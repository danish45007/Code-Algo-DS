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
    elif x > top(heap):
        heap.append(x)
    elif x < top(heap):
        heap.insert(0,x)

def pop(heap):
    if len(heap) == 0:
        return -1
    else:
        heap.pop()

if __name__ == "__main__":
    h = createHeap()
    push(h,7)
    push(h,10)
    push(h,4)
    push(h,11)
    pop(h)
    pop(h)
    pop(h)
    print(top(h))


