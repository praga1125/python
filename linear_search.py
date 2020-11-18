def search(arr, target):
    temp = 0
    while len(arr) > 0 and temp < len(arr):
        if target == arr[temp]:
            return temp
        else:
            temp += 1


array = [9, 0, 12, 1, 3, 2, 8, 4]
value = 22
ans = search(array, value)
if ans is not None:
    print("The element "+str(value)+" is found at index of "+str(ans))
else:
    print("The target element is not in array")