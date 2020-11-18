arr = [3, 4, 2, 7, 1, 0]
n = len(arr)
for i in range(n):
    temp = i
    for j in range(i+1, n):
        if arr[temp] > arr[j]:
            temp = j
        arr[i], arr[temp] = arr[temp], arr[i]
        

print(arr)