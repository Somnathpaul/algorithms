#               1
#           /       \  
#          2          3  
#         /  \      /   \
#        4    5     6   7 


# node 
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# tree
class Tree(object):
    def __init__(self, root):
        self.root = Node(root)
        

    # node visiting parten 
    """ left root right """
    def inorder(self, root):
        if root:
            #recur to the left value
            self.inorder(root.left)
            # print the right value
            print(root.value)
            #recur to the right value
            self.inorder(root.right)

tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

tree.inorder(tree.root)