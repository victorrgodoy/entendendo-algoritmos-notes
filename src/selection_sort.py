#sort array with selection
#big o: O(n**2)

def find_min_value(array):     
    index = 0
    value = array[index]
    for i in range(1, len(array)):
        if value > array[i]:
            value  = array[i]
            index = i
    return index

def selection_sort(array):
    new_array = []
    for _ in range(len(array)):
        min_index = find_min_value(array)
        new_array.append(array.pop(min_index))
    return new_array
            
array = [5,3,2,4,1]
print(f'Array sort: {selection_sort(array)}')