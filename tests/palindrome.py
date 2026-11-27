def palindrome(s):
    reversed = ""
    for char in s:
        reversed = char  + reversed
        
    if s == reversed:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")
palindrome("MADAM")