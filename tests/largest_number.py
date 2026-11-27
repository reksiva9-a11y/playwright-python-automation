def largest(num):
    largest = float("-inf")
    for n in num:
        if n > largest:
            largest = n
    return largest

largest_number = largest([1,2,3,4,5,6,7,8,9])
print("Largest number in the list is:", largest_number)