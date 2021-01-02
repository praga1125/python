def remove_duplicates(numbers):
    i = 0
    temp = []
    for number in numbers:
        if number not in temp:
            temp.append(number)
    return temp


numbers = [11, 22, 11, 22, 4, 2, 1, 4, 2, 4, 11]
print(f'The original list : {numbers}')
ans = remove_duplicates(numbers)
print(f'The removed duplicate list : {ans}')
