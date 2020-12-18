def monotonic_array(array):
    no_decreasing = True
    no_increasing = True
    for i in range (1, len(array)):
        if array[i] <= array[i-1]:
            no_increasing = False
        if array[i] >= array[i-1]:
            no_decreasing = False
    return no_decreasing or no_increasing


arr = [1, 2, 4, 5, 6, 7]
ans = monotonic_array(arr)
if ans:
    print("It is monotonic array")
else:
    print("It is non monotonic array")
