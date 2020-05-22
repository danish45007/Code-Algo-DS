def countRotations(arr,low, high): 
  
    # This condition is needed to  
    # handle the case when array 
    # is not rotated at all 
    if (high < low): 
        return 0
  
    # If there is only one  
    # element left 
    if (high == low): 
        return low 
  
    # Find mid 
    # (low + high)/2  
    mid = low + (high - low)/2;  
    mid = int(mid) 
  
    # Check if element (mid+1) is 
    # minimum element. Consider  
    # the cases like {3, 4, 5, 1, 2} 
    if (mid < high and arr[mid+1] < arr[mid]): 
        return (mid+1) 
  
    # Check if mid itself is  
    # minimum element 
    if (mid > low and arr[mid] < arr[mid - 1]): 
        return mid 
  
    # Decide whether we need to go 
    # to left half or right half 
    if (arr[high] > arr[mid]): 
        return countRotations(arr, low, mid-1); 
  
    return countRotations(arr, mid+1, high)



def binarySearch(arr, l, r, x): 
  
    while l <= r: 
        
        # To avoid the init overflow
        mid = l + (r - l)//2; 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            pvoit =  mid
            return pvoit 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element was not present 
    return -1










arr = [4,5,6,7,0,1,2]
target = 0
s = 0
N = len(arr)
end = N-1

pivot = (countRotations(arr,0,N-1))
# arr_1 = arr[0:pivot]
# arr_2 = arr[pivot:end+1]


sol1 = (binarySearch(arr,0,pivot-1,target))
sol2 = (binarySearch(arr,pivot,len(arr)-1,target))

print(sol2)