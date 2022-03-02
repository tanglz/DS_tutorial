class CNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class CLinkedList:
    def __init__(self):
        self.head = None

    # insert a node at the end of the list
    def insert(self, data):
        new_node = CNode(data)  # create a new node with data= data
        if self.head is None:
            self.head = new_node
        else:
            current = self.head  # find the last node, start from head
            while current.next_node is not self.head:
                current = current.next_node
            current.next_node = new_node
        new_node.next_node = self.head

    # insert a node at the end of the list
    def insert_node(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head  # find the last node, start from head
            while current.next_node is not self.head:
                current = current.next_node
            current.next_node = node
        node.next_node = self.head

    def len(self):
        cnt = 0
        current = self.head
        if current:
            cnt = 1
        while current.next_node is not self.head:
            cnt = cnt + 1
            current = current.next_node
        return cnt

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

    # convert to list
    def tolist(self):
        l = []
        current = self.head
        while current and current.next_node is not self.head:
            l.append(current.data)
            current = current.next_node
        l.append(current.data)
        return l


# # Create a linked list with one node (head)
# ll = CLinkedList()
# ll.insert(3)
# # Insert a node
# ll.insert(4)
# ll.insert(5)
# ll.insert(6)
# ll.insert(7)
# # to list for printing
# print(ll.tolist())