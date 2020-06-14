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
        self.helper = Helper()

    # postorder function
    """ Left->Right->Root """
    def postorder(self, root):
        if root:
            # recur to the left value
            self.postorder(root.left)
            # recur to the right value
            self.postorder(root.right)
            # push the root value into the helper class list
            self.helper.push(root.value)
            #print(root.value)

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

tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

tree.postorder(tree.root)

# below function will get call from test file
#tree.helper.print()