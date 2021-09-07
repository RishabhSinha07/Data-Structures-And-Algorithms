# Python program for implementation of Count Sort

'''
Time Complexity: O(n+k) where n is the number of elements in input array and k is the range of input. 
Auxiliary Space: O(n+k)

Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (kind of hashing). Then doing some arithmetic to calculate the position of each object in the output sequence.
Let us understand it with the help of an example. 

Its running time is linear in the number of items and the difference between the maximum key value and the minimum key value, so it is only suitable for direct use in situations where the variation in keys is not significantly greater than the number of items

'''
def countSort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    
    range_of_elements = max_element - min_element + 1

    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]


    for data in arr:
        count_arr[data-min_element]+=1
    
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
    
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
    
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]

    return arr

if __name__ == "__main__":
    arr = [9,8,7,6,5,4,1111]
    print(countSort(arr))

