def checker(statement):
    vowels = ['a', 'e', 'i', 'o', 'u']
    temp = []
    for i in statement:
        for j in vowels:
            if i == j:
                temp += i
    return temp


words = input("enter the statement to check : ")
ans = checker(words)
if not ans:
    print("statement does not contains vowels")
else:
    print(f'The vowels in the statement are : {ans}')
