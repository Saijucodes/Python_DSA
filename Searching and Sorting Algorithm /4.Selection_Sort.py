def selection_sort(lst):
    # Your code goes here
    for i in range(len(lst) - 1):
        current_min = lst[i]
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < current_min:
                current_min = lst[j]
                min_index = j 
        lst[i],lst[min_index] = current_min,lst[i]
    
    return lst


#Simpler

def selection_sort(lst):
    # Your code goes here
    for i in range(len(lst) - 1):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j 
        lst[i],lst[min_index] = lst[min_index],lst[i]
    
    return lst
