def dict_to_list(my_dict):
    list_1 = []
    for k, v in my_dict.items():
        if isinstance(v,int):
            v *= 2
        list_1.append((k,v))
    return list_1

print(dict_to_list({'a': 15, 'b': 2.4, 'c': [], 'd':'asd','e': 395}))








