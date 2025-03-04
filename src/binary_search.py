#search a value more fast
#list must be sorted
#big o: O(log n)

array = [100,200,300,400,500,600,700,800,900,1000]
value = 1000

def search_binary(array, value):
    steps = 0
    start = 0
    end = len(array) - 1
    while start <= end:
        steps += 1
        i = (start + end) // 2
        if array[i] == value:
            return i, steps
        elif array[i] < value:
            start = i + 1
        else:
            end = i - 1
    return -1

index, steps = search_binary(array, value)
print(f'Index: {index}\nSteps: {steps}')
