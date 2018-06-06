def sort_stack(sta):
    smaller = 0
    tmp = stack()

    while not sta.isEmpty():
        if not tmp.isEmpty9) and tmp.peek() <= sta.peek():
            tmp.push(sta.pop())
        else:
            smaller = sta.pop()
            while not tmp.isEmpty() and smaller < tmp.peek():
                sta.push(tmp.pop())
            tmp.push(smaller)

    while not tmp.isEmpty():
        sta.push(tmp.pop())

    return sta
