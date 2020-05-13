# node of the tree
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# tree
class Tree(object):
    def __init__(self, root):
        self.root = Node(root)