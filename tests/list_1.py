def list_new(l):
     new_list = []
     for i in l:
       if i % 2 == 0:
        new_list.append(i)
     return new_list
lists = list_new([1,2,3,4,5,6,7,8,9])
print("List is:", lists)