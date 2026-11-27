def  duplicate_numbers(list):
    duplicates =[]
    seen = []
    for num in list:
         if num in seen:
            if num not in duplicates:
              duplicates.append(num)
         else:
            seen.append(num)
    return duplicates

duplicate_numberslist = duplicate_numbers([1,2,3,4,5,6,7,8,9,1,2,3])
print("Duplicate numbers in the list are:", duplicate_numberslist)