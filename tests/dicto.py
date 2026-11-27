def create_dict(keys):
    dict = {}

    for i in range(len(keys)):
        dict[keys[i]]  = i
    return dict
create_dict = create_dict(["a", "b", "c", "d", "e"])
print(create_dict)