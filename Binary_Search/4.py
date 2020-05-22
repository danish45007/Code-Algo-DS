
# Brute Force Solution

# from collections import Counter
# l = [2,4,10,10,10,18,20]
# target = 10

# d = Counter(l)
# print(d[target])


# Binary Search Solution

def first(arr, low, high, x, n) : 
    if(high >= low) : 
        mid = low + (high - low) // 2
        if( ( mid == 0 or x > arr[mid - 1]) and arr[mid] == x) : 
            return mid 
        elif(x > arr[mid]) : 
            return first(arr, (mid + 1), high, x, n) 
        else : 
            return first(arr, low, (mid - 1), x, n) 
      
    return -1


def last(arr, low, high, x, n) : 
    if (high >= low) : 
        mid = low + (high - low) // 2
        if (( mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x) : 
            return mid 
        elif (x < arr[mid]) : 
            return last(arr, low, (mid - 1), x, n) 
        else : 
            return last(arr, (mid + 1), high, x, n) 
              
    return -1



if __name__ == "__main__":
    arr = [2,4,10,10,10,18,20]
    target = 10
    low = 0
    high = len(arr)-1
    n = len(arr)
    low_index = first(arr,low,high,target,n)
    high_index = last(arr,low,high,target,n)
    print(low_index)
    print(high_index)
    count = 0

    for i in range(low_index,high_index+1):
        count = count+1
    print(count)


