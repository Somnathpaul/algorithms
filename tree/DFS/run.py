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

traversal_inorder = []
traversal_postorder = []
traversal_preorder = []

def inorder(root): 
  
    if root: 
  
        # First recur on left child 
        inorder(root.left) 
  
        # then print the data of node 
        traversal_inorder.append(root.value), 
  
        # now recur on right child 
        inorder(root.right) 
    

# A function to do postorder tree traversal 
def postorder(root): 
  
    if root: 
  
        # First recur on left child 
        postorder(root.left) 
  
        # the recur on right child 
        postorder(root.right) 
  
        # now print the data of node 
        traversal_postorder.append(root.value)

# A function to do postorder tree traversal 
def preorder(root):
    if root:
        
        # First print the data of node 
        traversal_preorder.append(root.value), 
  
        # Then recur on left child 
        preorder(root.left) 
  
        # Finally recur on right child 
        preorder(root.right) 


# Set up tree:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)



def getData(traversal_type, root):
  if traversal_type == "inorder":
    inorder(root)
    return traversal_inorder
  
  elif traversal_type == "postorder":
    postorder(root)
    return traversal_postorder

  elif traversal_type == "preorder":
    preorder(root)
    return traversal_preorder
  else:
    print(traversal_type , "is not supported")
    return False


print(getData("inorder", root))
print(getData("preorder", root))
print(getData("postorder", root))