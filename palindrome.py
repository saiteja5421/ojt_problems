#  program to check if a string is palindrome or not


def palindrome(a):
    reverse = ""
    for letter in a:
        reverse = letter + reverse
    if a == reverse:
        print("its a palindrome")
    else:
        print("its not a palindrome")


palindrome("tweet")