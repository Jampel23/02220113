def quick_sort(arr):
    comparisons = 0
    swaps = 0
    
    def partition(arr, low, high):
        nonlocal comparisons, swaps
        # Using median-of-three to select pivot
        mid = (low + high) // 2
        pivot_candidates = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
        pivot_candidates.sort()  # Sort by value
        pivot_value, pivot_index = pivot_candidates[1]
        
        # Swap pivot to the end
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        swaps += 1
        
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            comparisons += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        
        # Place pivot in the correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        
        return i + 1
    
    def quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_recursive(arr, low, pi - 1)
            quick_sort_recursive(arr, pi + 1, high)

    quick_sort_recursive(arr, 0, len(arr) - 1)
    
    return arr, comparisons, swaps


# Example usage:
original_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list, num_comparisons, num_swaps = quick_sort(original_list)

print("Original List:", original_list)
print("Sorted using Quick Sort:", sorted_list)
print("Number of comparisons:", num_comparisons)
print("Number of swaps:", num_swaps)
