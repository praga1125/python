def move_elements(array, target):
    array.sort()
    left = 0
    right = len(array)-1
    while left < right:
        while left < right and array[right] == target:
            right -= 1
        if array[left] == target:
            array[left], array[right] = array[right], array[left]
        left += 1
    return array


arr = [99, 22, 22, 22, 10, 99, 99, 0]
element = 22
ans = move_elements(arr, element)
print(ans)
