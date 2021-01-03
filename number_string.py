def number_string(numbers):
    digits = {
         "1": "One",
         "2": "Two",
         "3": "Three",
         "4": "Four",
         "5": "Five",
         "6": "Six",
         "7": "Seven",
         "8": "Eight",
         "9": "Nine",
         "0": "Zero"
    }
    ans = ""
    for number in numbers:
        ans += digits.get(number)+" "
    return ans


numbers = input("enter numbers : ")
string = number_string(numbers)
print(string)
