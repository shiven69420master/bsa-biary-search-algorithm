def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

numbers = [2, 4, 6, 7, 9, 13, 19]
print(binary_search_recursive(numbers, 4, 0, len(numbers) - 1))   