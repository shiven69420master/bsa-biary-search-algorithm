def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low<=high:
        mid=(low+high) // 2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

data=[23, 54, 65, 76, 98, 102, 113]
print(binary_search(data, target=22))
print("The complexity of binary search alogrithm is O(log n)")        