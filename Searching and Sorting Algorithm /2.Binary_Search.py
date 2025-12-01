def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    mid = (start + end) // 2
    
    while(start <= end):
        if arr[mid] < target:
            start = mid + 1
        if arr[mid] > target:
            end = mid - 1
        if arr[mid] == target:
            return mid
        mid = (start + end) // 2
    
    return -1

print(binary_search([10,20,30,40,50,60] , 60))
    
