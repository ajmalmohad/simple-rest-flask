class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert_recursive(self,data,node):
        if data["id"] < node.data["id"]:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data,node.left)
        elif data["id"] > node.data["id"]:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data,node.right)
        else:
            return

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data,self.root)

    def _search_recursively(self,node,blog_post_id):
        if node.left and node.right is None:
            return False
        if blog_post_id == node.data['id']:
            return node.data

        if blog_post_id < node.data['id']:
            return self._search_recursively(node.left,blog_post_id)

        if blog_post_id > node.data['id']:
            return self._search_recursively(node.right,blog_post_id)

    def search(self,blog_post_id):
        blog_post_id = int(blog_post_id)
        if self.root is None:
            return False
        return self._search_recursively(self.root,blog_post_id)