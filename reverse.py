def reverse(arr, first, last):
    while first < last:
        arr[first], arr[last] = arr[last], arr[first]
        first += 1
        last -= 1


arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(f'The given array : {arr}')
reverse(arr, 0, len(arr)-1)
print(f'reversed array :  {arr}')
