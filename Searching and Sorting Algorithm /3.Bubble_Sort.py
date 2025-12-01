def bubble_sort(arr):
    
    for j in range(len(arr) - 1):
        for i in range(len(arr)-j - 1):
            if arr[i+1] < arr[i] :
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
    
    return arr
    

print(bubble_sort([11,12,25,90,13]))
    
