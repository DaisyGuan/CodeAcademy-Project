def digit_sum(n):
    dsum = 0
    while n > 0:
        r = n % 10
        dsum += r
        n = n/10
    else:
        return dsum
