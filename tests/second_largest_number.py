def second_largest_number(number):
    largest = float('-inf')
    second_largest = float('-inf')

    for num in number:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest
second = second_largest_number([1,8,9,7,4,11])
print("Second largest number in the list is:", second)