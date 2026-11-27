def even_odd(num):
    for n in  num:
        if n % 2 == 0:
            print(n, "is even")
        else:
            print(n, "is odd")
result = even_odd([1,2,3,4,5,6,7,8,9])
print("Even and odd numbers in the list are:", result)