#               1
#           /       \  
#          2          3  
#         /  \      /   \
#        4    5     6   7 


# node 
class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

# tree
class Tree(object):
    def __init__(self, root):
        # object for node called and passed with root value 
        self.root = Node(root)
        # object for helper function 

    # postorder function
    """ Left->Right->Root """
    def postorder(self, root):
        if root:
            # recur to the left value
            self.postorder(root.left)
            # recur to the right value
            self.postorder(root.right)
            # print the root value 
            print(root.value)


tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

tree.postorder(tree.root)