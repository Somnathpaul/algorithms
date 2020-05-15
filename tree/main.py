
#               1
#           /       \  
#          2          3  
#         /  \      /   \
#        4    5     6   7 

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
    
    def print(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder(tree.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder(self, start, traversal):
        # node visiting pattern
        """Root->Left->Right"""

        if start:
            traversal = traversal + (str(start.value) + "-")
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)

        return traversal
 
    def postorder(self, start, traversal):
        # node visiting parten 
        """ Left->Right->Root """
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal = traversal + (str(start.value) + "-")

        return traversal



# Set up tree:
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print("preorder"))
print(tree.print("postorder"))