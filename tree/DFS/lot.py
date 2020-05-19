# level order traversal : breadth first search 
class Queue(object):
    def __init__(self, value):
        self.items = []

    def enqueue(self, value):
        self.items.insert(0, value)

    def dequeue(self, value):
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


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def lot(self, start):
        


