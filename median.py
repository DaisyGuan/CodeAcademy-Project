def median(n_list):
    new_list = sorted(n_list)
    if len(new_list) == 1:
        return 1
    else:
        if len(new_list) % 2 == 1:
            return new_list[len(new_list)/2]
        else:
            s = new_list[(len(new_list)+1)/2] + new_list[(len(new_list)+1)/2-1]
            return s / 2.0
