def small(num):
    small = float("inf")
    for n in num:
       if n < small:
          small = n
    return small
small = small([1,2,3,4,5,6,7,8,9])
print("Smallest number in the list is:", small)