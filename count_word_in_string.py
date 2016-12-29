def count(sequence,item):
    found = 0
    sqc = list(sequence)
    for w in sqc:
        if w == item:
            found += 1
    
    return found
    
