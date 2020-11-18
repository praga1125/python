def swap(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pivot = swap(array, low, high)
        quick_sort(array, low, pivot-1)
        quick_sort(array, pivot+1, high)


arr = [8, 0, 9, 1, 4, 5, 7]
n = len(arr)
quick_sort(arr, 0, n-1)
print("The sorted element are :")
print(arr)
