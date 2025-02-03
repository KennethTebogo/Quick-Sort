def quick_sort(arr):
    # Base case: if the array is empty or has one element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose the pivot element (here, we pick the last element)
    pivot = arr[-1]
    
    # Partition the array into two sub-arrays: less than pivot, and greater than pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # Recursively apply quick_sort to the left and right sub-arrays, and combine the results
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)

