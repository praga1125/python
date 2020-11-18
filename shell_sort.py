
def shell_sort(arr):
    n = len(arr)
    space = n // 2
    while space > 0:
        for i in range(space, n):
            temp = arr[i]
            j = i
            while j >= space and arr[j - space] > temp:
                arr[j] = arr[j - space]
                j -= space
            arr[j] = temp
        space //= 2


arr = [9, 0, 1, 5, 7, 8, 6]
shell_sort(arr)
print("The sorted values are :")
print(arr)
