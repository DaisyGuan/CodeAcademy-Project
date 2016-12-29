def remove_duplicates(n_list):
    new_list = []
    for a in n_list:
        while a not in new_list:
            new_list.append(a)
    return new_list
