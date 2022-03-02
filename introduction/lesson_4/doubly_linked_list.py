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

    def len(self):
        cnt = 0
        current = self.head
        while current:
            cnt = cnt + 1
            current = current.next_node
        return cnt

    def get_first(self):
        return self.head

    def get_last(self):
        current = self.head
        while current.next_node:
            current = current.next_node
        return current

    def get_index(self, index):
        i = 0
        current = self.head
        while current:
            if i == index:
                return current
            current = current.next_node
            i = i + 1
        # if can't find an item
        raise IndexError("Index out of range")

    # reverse
    def reverse(self):
        temp = None
        current = self.head
        # Swap next and prev for all nodes
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        # change head
        if temp is not None:
            self.head = temp.prev

    # convert to list
    def tolist(self):
        l = []
        current = self.head
        while current:
            l.append(current.data)
            current = current.next_node
        return l

    def inset_node(self, node):
        if self.head is None:
           self.head = node
        else:
            current = self.head  # find the last node, start from head
            while current.next_node:
                current = current.next_node
            current.next_node = node

# # Create a linked list with one node (head)
# ll = DLinkedList()
# # Insert a node
# ll.insert(4)
# ll.insert(5)
#
# # to list for printing
# print(ll.tolist())