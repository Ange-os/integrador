def calc_max(n1,n2):
    while n2:
        n1, n2 = n2, n1 % n1
    return n1