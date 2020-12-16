def three_sum(arr, target):
    arr.sort()
    ans = []
    for curr in range(len(arr) - 2):
        left = arr[curr] + 1
        right = len(arr) - 1
        while left < right:
            curr_sum = arr[curr] + arr[left] + arr[right]
            if curr_sum == target:
                ans.append([arr[curr], arr[left], arr[right]])
                left += 1
                right -= 1
            elif curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
    return ans


arr = [55, 44, 88, 11, 00, 12, 66, 23, 33]
target = 99
print(three_sum(arr, target))

