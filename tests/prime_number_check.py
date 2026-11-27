def primenumber(num):
     if num <=1:
          print("The number is not prime")
     else:
          for i in range(2,num):
               if num % i == 0:
                    print("The number is not prime")
                    return
          print("The number is prime")

primenumber(9)

          