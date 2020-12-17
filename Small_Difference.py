def small_difference(arr_0, arr_1):
    arr_0.sort()
    arr_1.sort()
    pointer0 = 0
    pointer1 = 0
    small = float("inf")
    current = float("inf")
    ans = []
    while pointer0 < len(arr_0) and pointer1 < len(arr_1):
        first_num = arr_0[pointer0]
        second_num = arr_1[pointer1]
        if first_num < second_num:
            current = second_num - first_num
            pointer0 += 1
        elif second_num < first_num:
            current = first_num - second_num
            pointer1 += 1
        else:
            return [first_num, second_num]
        if small > current:
            small = current
            ans = [first_num, second_num]
    return ans


array_0 = [9, 8, 7, 1, 0]
array_1 = [10, 11, 22, 2]
answer = small_difference(array_0, array_1)
print(answer)
