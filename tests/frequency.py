def frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
frequency = frequency("APPLE")
print("Frequency of characters in the string is:", frequency)


    