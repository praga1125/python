def two_sum(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        sum1 = arr[left] + arr[right]
        if sum1 == target:
            return [arr[left], arr[right]]
        elif sum1 < target:
            left += 1
        elif sum1 > target:
            right -= 1
    return []


arr = [9, 6, 3, 5, 2, 0, 55, 22]
target = 0
print(two_sum(arr, target))
