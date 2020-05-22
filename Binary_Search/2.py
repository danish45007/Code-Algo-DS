def binarySearch(arr, l, r, x): 
  
    while l <= r: 
        
        # To avoid the init overflow
        mid = l + (r - l)//2; 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element was not present 
    return -1
    

if __name__ == "__main__":
    arr = [20,15,10,5,1]
    arr = sorted(arr,reverse=False)
    target = 5
    l = 0
    r = len(arr)-1
    print(binarySearch(arr,l,r,target))



