# Python program for implementation of Selection Sort

'''
This method moves in forward direction
For each iteration we select the starting object as the target value
We then iterate from current position to the last postion and find the index of smallest element
We swap the position of current and smallers element
'''
def selectionSort(arr):
    for i in range(len(arr)):
        smallestElement = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                smallestElement = j 
        if smallestElement != i:
            arr[i],arr[smallestElement] = arr[smallestElement],arr[i]
    return arr
        
if __name__ == "__main__":
    arr = [9,8,7,6,5,4]
    print(selectionSort(arr))

