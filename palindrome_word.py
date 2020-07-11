word = input("enter the word to check: ")
def isPalindrome(str): 

    for i in range(0, int(len(str)/2)):  

        if str[i] != str[len(str)-i-1]: 

            return False

    return True


ans = isPalindrome(word)  

if (ans): 

    print("this word is palindrome") 

else: 

    print("this is not a palindrome") 
