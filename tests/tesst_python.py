def reverse_string(string):
    text = string
    reverse = ""
    for char in text:
        reverse = char + reverse
    return reverse
reversed = reverse_string("EPAM Systems")
print("reverse string", reversed)