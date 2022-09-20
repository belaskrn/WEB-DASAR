def palindrome(string):
    return string == string[::-1]

if palindrome("rotator"):
    print("True")
else:
    print("False")