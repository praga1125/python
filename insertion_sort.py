values = [8, 0, 2, 7, 9, 1]


def insert_sort(arr):
    for j in range(1, len(arr)):
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1


insert_sort(values)
print("The sorted values are :")
print(values)