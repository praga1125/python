def bubble_sort(value):
    n = len(value)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if value[j] > value[j+1]:
                value[j], value[j+1] = value[j+1], value[j]


arr = [9, 6, 3, 8, 1, 0]
bubble_sort(arr)
print("The sorted array list :")
print(arr)

