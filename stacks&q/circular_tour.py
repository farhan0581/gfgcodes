def tour(lis, n):
    remain = 0
    start = s = 0
    
    for i, elem in enumerate(lis):
        s += elem[0] - elem[1]
        if s < 0:
            start = i+1
            remain += s
            s = 0
    
    if remain + s >= 0:
        return start
    else:
        return -1