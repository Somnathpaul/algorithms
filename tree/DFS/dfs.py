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
    self.root = Node(root)
    # object of helper function
    self.output = Output()
  

  # postorder function
  """ Left->Right->Root """
  def postorder(self, root):
    if root:

      # First recur on left child 
      self.postorder(root.left) 
  
      # the recur on right child 
      self.postorder(root.right) 
  
      # now print the data of node 
      self.output.postorder_push(root.value)
      #print(root.value)


  def preorder(self, root):
    if root:

      # preorder function
      """root -> left -> right"""

      # print the root value 
      self.output.preorder_push(root.value)
      #print(root.value)

      # recur left value
      self.preorder(root.left)

      # recur the right value
      self.preorder(root.right)


# helper function
class Output(object):
  def __init__(self):
    self.traversal_postorder = []
    self.traversal_preorder = []
  
  def postorder_push(self, value):
    self.traversal_postorder.append(value)

  def preorder_push(self, value):
    self.traversal_preorder.append(value)
  
  def show(self):
    print("postorder: ",self.traversal_postorder)
    print(self.traversal_preorder)
    print(self.size())

  def size(self):
    return len(self.traversal_postorder)

  def __len__(self):
    return self.size()



# Set up tree:
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


tree.preorder(tree.root)
tree.postorder(tree.root)
tree.output.show()

