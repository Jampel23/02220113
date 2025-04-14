def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0
    
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        
        if arr[mid] == target:
            return mid, comparisons  # Found the target
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1, comparisons  # Target not found


def binary_search_recursive(arr, target, low=0, high=None, comparisons=0):
    if high is None:
        high = len(arr) - 1
    
    if low > high:
        return -1, comparisons  # Target not found
    
    mid = (low + high) // 2
    comparisons += 1
    
    if arr[mid] == target:
        return mid, comparisons  # Found the target
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high, comparisons)
    else:
        return binary_search_recursive(arr, target, low, mid - 1, comparisons)


# Example usage
arr = [12, 23, 34, 45, 56, 67, 89]
target = 67

print("Sorted List:", arr)
print(f"Searching for {target} using Iterative Binary Search:")
index, comparisons = binary_search_iterative(arr, target)
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")
print(f"Number of comparisons: {comparisons}\n")

print(f"Searching for {target} using Recursive Binary Search:")
index, comparisons = binary_search_recursive(arr, target)
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")
print(f"Number of comparisons: {comparisons}")
