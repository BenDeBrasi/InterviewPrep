def CheckBalanced(Tree):
    
    if not Tree:
        return True

    Left = GetHeight(Tree.left)
    Right = GetHeight(Tree.right)

    if Left == Right or abs(Left - Right) == 1:
        return CheckBalanced(Tree.left) and CheckBalanced`(Tree.right)
    else:
        return False


def GetHeight(Tree):

    if not Tree:
        return 0
    else:
        LeftHeight = GetHeight(Tree.left)
        RightHeight = GetHeight(Tree.right)
        
        if LeftHeight >= RightHeight:
            return LeftHeight + 1
        else:
            return RightHeight + 1
