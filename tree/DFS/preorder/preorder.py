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
        self.helper = Helper()

    # preorder function
    # """root -> left -> right"""
    def preorder(self, root):
        if root:
            # push the root value into helper function list
            self.helper.push(root.value)
            # recur to the left root
            self.preorder(root.left)
            # recur to the right root
            self.preorder(root.right)

# helper class 
class Helper(object):
    def __init__(self):
        self.traversal = []
    
    def push(self, value):
        self.traversal.append(value)

    def print(self):
        #print(self.traversal)
        return self.traversal
    
    def size(self):
        return len(self.traversal)
    
    def __len__(self):
        return self.size()





# creating the tree
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

tree.preorder(tree.root)

# (tree.helper.print())