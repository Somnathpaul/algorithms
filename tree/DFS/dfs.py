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

class Output(object):
  def __init__(self):
    self.traversal = []
  
  def push(self, value):
    self.traversal.append(value)
  
  def show(self):
    return self.traversal

class Tree(object):
  def __init__(self, root):
    self.root = Node(root)  

  # postorder function
  """ Left->Right->Root """
  def postorder(self, root):
    # First recur on left child 
    self.postorder(root.left) 
  
    # the recur on right child 
    self.postorder(root.right) 
  
    # now print the data of node 
    output = Output()
    output.push(root.value)
    #self.traversal.append(root.value, self.traversal)
    print(root.value)
  



# Set up tree:
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

obj = Output()
tree.postorder(tree.root)
print(obj.show())

