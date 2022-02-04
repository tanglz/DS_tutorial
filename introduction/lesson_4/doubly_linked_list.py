class DNode:
    def __init__(self, data, next_node=None, pre_node=None):
        self.data = data
        self.next_node = next_node
        self.pre_node = pre_node


class DLinkedList:
    def __init__(self):
        self.head = None

    # insert a node at the end of the list
    def insert(self, data):
        new_node = DNode(data)  # create a new node with data= data
        if self.head is None:
            self.head = new_node
        else:
            current = self.head       # find the last node, start from head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
            new_node.pre_node = current

    # convert to list
    def tolist(self):
        l = []
        current = self.head
        while current:
            l.append(current.data)
            current = current.next_node
        return l



# Create a linked list with one node (head)
ll = DLinkedList()
# Insert a node
ll.insert(4)
ll.insert(5)

# to list for printing
print(ll.tolist())