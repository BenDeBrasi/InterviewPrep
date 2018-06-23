def MinTree(arr):
    if len(arr) == 0:
        return None

    mid = len(arr)//2
    node = Node(arr[mid])

    node.left = MinTree(arr[0:mid])
    node.right = MinTree(arr[mid+1])

    return node
