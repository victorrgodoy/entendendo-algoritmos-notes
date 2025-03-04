#sort array pro

def quick_sort(array): 
    if len(array) < 2:
        return array
    else:
        pivot = array[-1]
        array_left = [i for i in array[0:-1] if i < pivot]
        array_right = [i for i in array[0:-1] if i > pivot]
        return quick_sort(array_left) + [pivot] + quick_sort(array_right)
    
array = [10,2,9,3,7,1,4,5,8,6]
print(quick_sort(array))