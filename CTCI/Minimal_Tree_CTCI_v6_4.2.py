def MinTree(arr):
    if len(arr):
        return None
    s=0
    e=len(arr)-1
    mid = s + (e-s)/2
    Root=Node(arr[mid))
    Root.left = MinTree(arr[s,mid])
    Root.right = MinTree(arr[mid+1,e])
    return Root
