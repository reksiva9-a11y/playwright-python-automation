def non_repeat_first(s):
    string = {}

    for char in s:
        if char in string:
            string[char] +=1
        else:
            string[char] = 1
    for key,value in string.items():
        if value == 1:
            return key

    return None

result = non_repeat_first("automation")
print("first non repaeting:",result)
