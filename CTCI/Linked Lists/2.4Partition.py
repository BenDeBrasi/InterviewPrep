def Partition(LL,part):
    LL1 = LL()
    LL2 = LL()

    tmp = LL.head
    while tmp != None:
        if tmp.data < part:
            LL1.add(tmp)
        else:
            LL2.add(tmp)
        LL1.tail.add(LL2)
        return LL1
