# level order traversal : breadth first search 
class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.insert(0, value)

    def dequeue(self):
        self.items.pop()
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    
    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "levelorder":
            return self.levelorder(tree.root, "")

        else:
            print("Traversal type " , str(traversal_type), "is not supported")



    def levelorder(self, start):
        if start is None:
            return 
        
        queue = Queue()
        queue.enqueue(start)
        traversal  = ""

        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal
    
    
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.print_tree("levelorder"))






