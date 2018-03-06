def perm(string):
    result = []
    if len(string) == 0:
        return result

    for i in xrange(0,len(string)):
        new = string[:i] + string[i+1:]
        master = perm(new)

        for s in master:
            master.append(string[i] + s)

    return result

print(perm([1,2,3]))
