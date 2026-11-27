def reverse_string_index(s):

    string = s
    reversed_string =""
    for i in range(len(string)):
       reversed_string = string[i] + reversed_string
    return reversed_string
reverse_string = reverse_string_index("EPAM Systems")
print("REVERSED STRING", reverse_string)
