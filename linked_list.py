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

    # Linked List to Array
    def to_list(self):
        list = []
        if self.head is None:
            return list
        node = self.head
        while(node):
            list.append(node.data)
            node = node.next_node
        return list

    # Print Linked List
    def print_ll(self):
        ll_string=''
        node = self.head
        # Empty Linked List
        if node is None:
            print(None)
        # Non Empty Linked List
        while(node):
            ll_string += f' {str(node.data)} =>'
            node = node.next_node
        ll_string += ' None'
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

    def get_user_by_id(self,user_id):
        node = self.head
        while(node):
            if node.data['id'] is int(user_id):
                return node.data
            node = node.next_node
        return None