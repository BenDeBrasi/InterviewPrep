def BuildOrder(p,d):
    edges = d #copy.deepcopy(d) note
    prev = 0
    curr = []
    
    while prev != len(edges):
        prev = len(edges)
        for n in p:
            for e in edges:
                if e[1] == n:
                    break
                if e == edges[-1]:
                    curr.append(n)
                    for x in edges:
                        if x[0] == n:
                            edges.remove(x)
                            if len(edges) == 0:
                                for n in p:
                                    if n not in curr:
                                        curr.append(n)
                                return curr
    return [-1] #Arbitrary error code


p = ['a','b','c']
d = [('a','b'),('b','c'),('b','a')]
print(BuildOrder(p,d))
