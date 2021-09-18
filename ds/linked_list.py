# Linked List Node 
class Node:
    def __init__(self, data=None, next_node=None) :
        self.data = data
        self.next_node = next_node
    
# Linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    # Insert at Beginning
    def insert_head(self,data):
        node = Node(data,self.head)
        self.head = node

ll = LinkedList()
ll.insert_head(10)
print(vars(ll))