def purify(numbers):
    n_list = []
    for n in numbers:
        if n % 2 == 1:
            del n
        else:
            n_list.append(n)
    return n_list
