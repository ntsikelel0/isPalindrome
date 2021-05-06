"""
SCENARIO: Input a palindrome word

"""

c1= "MOM"   #declaring and assigning a string variable


#The definition of isPalindrome function
def isPalindrome(c):
    if c == c[::-1]:
        print("Yes! {} reversed is {}".format(c,c))
    else:
        print("No! {} reversed is {}".format(c,c))


isPalindrome((c1))      #calling the function