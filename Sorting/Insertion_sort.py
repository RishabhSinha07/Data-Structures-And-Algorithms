# Python program for implementation of Insertion Sort

'''
This method move in forward direction in an unsorted array. 
The iteration starts from pos 1 and the element at pos 0 is prev
For each current element, we want to move it back untill there is no smaller element behind it.
For this purpose we save the current value and keep moving the new previous elements untill we reach -1 or we find a value that is smaller than current
Then we insert the current saved value to that position and continue
'''
def insertionSort(arr):
    for i in range(1,len(arr)):
        token = arr[i]
        prev = i-1
        while prev >= 0 and arr[prev] >= token:
            arr[prev+1] = arr[prev]
            prev-=1
        arr[prev+1] = token  
    return arr
        
if __name__ == "__main__":
    arr = [9,8,7,6,5,4]
    print(insertionSort(arr))

