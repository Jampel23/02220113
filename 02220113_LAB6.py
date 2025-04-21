def merge_sort(arr):
    
    metrics = {'comparisons': 0, 'accesses': 0}
    
    def merge(left, right):
        merged = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            metrics['comparisons'] += 1  # Comparing elements
            metrics['accesses'] += 2  # Accessing left[i] and right[j]
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        # Remaining elements
        while i < len(left):
            merged.append(left[i])
            metrics['accesses'] += 1
            i += 1
        
        while j < len(right):
            merged.append(right[j])
            metrics['accesses'] += 1
            j += 1
        
        return merged

    def divide(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = divide(arr[:mid])
        right = divide(arr[mid:])
        return merge(left, right)

    sorted_arr = divide(arr)
    return sorted_arr, metrics['comparisons'], metrics['accesses']

original = [38, 27, 43, 3, 9, 82, 10]
sorted_arr, comparisons, accesses = merge_sort(original)

print("Original List:", original)
print("Sorted using Merge Sort:", sorted_arr)
print("Number of comparisons:", comparisons)
print("Number of array accesses:", accesses)
