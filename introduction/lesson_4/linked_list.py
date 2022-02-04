# singly linked list
#  a linked list is a string of nodes
#  each node containing both data and a reference to the next node

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    # insert a node at the end of the list
    def insert(self, data):
        new_node = Node(data)  # create a new node with data= data
        if self.head is None:
            self.head = new_node
        else:
            current = self.head       # find the last node, start from head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    # convert to list
    def tolist(self):
        l = []
        current = self.head
        while current:
            l.append(current.data)
            current = current.next_node
        return l


# Create a linked list with one node (head)
ll = LinkedList()
# Insert a node
ll.insert(4)
ll.insert(5)

# to list for printing
print(ll.tolist())