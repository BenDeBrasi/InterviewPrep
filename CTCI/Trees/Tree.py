class Node:
    def __init__(self, data, left = None, right = None, visited = False):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root = None):
        self.root = root

    def add(self, node):
        tree = self.root 
        while tree is not None:
            if node.data < tree.data:
                if tree.left == None:
                    tree.left = node
                    break
                else:
                    tree = tree.left
            else:
                if tree.right == None:
                    tree.right = node
                    break
                else:
                    tree = tree.right
