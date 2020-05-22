def BinarySearch(list,key):
    low = 0
    high = len(list)-1
    Found = False
    while low<=high and not Found:
        middle = (low+high)//2
        if key == list[middle]:
            Found = True
        elif key > list[middle]:
            low = middle+1
        else:
            high = middle-1
    if Found == True:
        print("Key is Found")
    else:
        print("Key not found")

list = [23,4,5,6,2,1]
list.sort()
key = int(input("Enter the key:"))
print(BinarySearch(list,key))
