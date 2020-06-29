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

class Queue(objcet):
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append



class Tree(object):
    def __init__(self, root):
        if root is None:
            return 
        
        # create a object of Queue
        Queue = Queue()