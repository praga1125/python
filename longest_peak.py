def peak(arr):
    longest_peak = 0
    i = 1
    while i < len(arr) - 1:
        peak = arr[i-1] < arr[i] and arr[i] > arr[i+1]
        if not peak:
            i += 1
            continue

        leftindex = i - 2
        while leftindex >= 0 and arr[leftindex] < arr[leftindex + 1]:
            leftindex -= 1
        rightindex = i + 2
        while rightindex < len(arr) and arr[rightindex] < arr[rightindex - 1]:
            rightindex += 1

        current_peak = rightindex - leftindex - 1
        longest_peak = max(longest_peak, current_peak)
        i = rightindex
    return longest_peak


array = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print("The length of longest peak element :  "+str(peak(array)))
