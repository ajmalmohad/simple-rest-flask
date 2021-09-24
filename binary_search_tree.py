class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert_recursive(self,value,node):
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(value,node.left)
        elif value > node.data:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(value,node.right)
        else:
            return

    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value,self.root)



bts = BinarySearchTree()
bts.insert(20)
bts.insert(10)
bts.insert(12)
bts.insert(5)
bts.insert(2)
bts.insert(3)
bts.insert(30)
bts.insert(25)
bts.insert(50)