#               1
#           /       \  
#          2          3  
#         /  \      /   \
#        4    5     6   7 

class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Tree(object):
    def __init__(self, root):
        # passing the value of root into object of node 
        self.root = Node(root)
        # object for helper function

    # preorder function
    # """root -> left -> right"""
    def preorder(self, root):
        if root:
            print(root.value)
            self.preorder(root.left)
            self.preorder(root.right)

# creating the tree
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

tree.preorder(tree.root)