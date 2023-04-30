def palindrome(string):
    if string == string[::-1]:
        print('palindrome.')
    else:
        print('not a palindrome.')

palindrome(input("Enter a string:"))

