def stepPerms(n):
    list_ = [1,2,4]

    for x in range(1, n):
        s = sum(list_[-3:])
        list_.append(s)
    
    return list_[n-1]