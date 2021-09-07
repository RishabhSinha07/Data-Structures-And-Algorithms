# Python program for implementation of Bubble Sort

'''
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
'''
def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    
    return arr
        
if __name__ == "__main__":
    arr = [9,8,7,6,5,4]
    print(bubbleSort(arr))

