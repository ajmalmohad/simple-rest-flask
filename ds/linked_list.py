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

    # Print Linked List
    def print_ll(self):
        ll_string=''
        node = self.head
        # Empty Linked List
        if node is None:
            print(None)
        # Displayed as String
        while(node):
            ll_string += f' {str(node.data)} =>'
            node = node.next_node
        ll_string += ' None'
        # Print Linked List
        print(ll_string)

    # Insert at Beginning
    def insert_head(self,data):
        if self.head is None:
            self.head = Node(data,None)
            self.last_node = self.head
            return

        new_node = Node(data,self.head)
        self.head = new_node

    # Insert at End
    def insert_tail(self,data):
        # If Linked List is Empty
        if self.head is None:
            self.insert_head(data)
            return
        
        self.last_node.next_node = Node(data,None)
        self.last_node = self.last_node.next_node
        # If Last Node is None
        # if self.last_node is None:
        #     node = self.head
        #     while node.next_node:
        #         node = node.next_node
            
        #     node.next_node = Node(data,None)
        #     self.last_node = node.next_node
        
        # else:
        #     self.last_node.next_node = Node(data,None)
        #     self.last_node = self.last_node.next_node

        


ll = LinkedList()
ll.insert_tail(10)
ll.insert_tail(20)
ll.insert_tail(20)
ll.insert_tail(20)
ll.insert_tail(50)
ll.print_ll()