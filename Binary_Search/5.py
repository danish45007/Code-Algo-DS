def Count(arr,start,end,N):


    while(start<=end):

        mid = start + (end-start)//2

        next = (mid+1)%N
        prev = (mid+N-1)%N
        
        if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
            return mid
        
        elif arr[start] <= arr[mid]:
            start = mid+1
        
        elif arr[mid] <= arr[end]:
            end = mid-1
    return -1

if __name__ == "__main__":
    arr = [11,12,15,18,2,5,6,8]
    n = len(arr)
    s = 0
    e = len(arr)-1
    print(Count(arr,s,e,n))

