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
            current = self.head  # find the last node, start from head
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

    def remove_index(self,index):
        if index == 0:  # remove first node
            self.head = self.get_index(1)
        elif index == self.len()-1: # remove last node
            self.get_index(index-1).next_node = None
        else:
            self.get_index(index-1).next_node = self.get_index(index+1)


# # Create a linked list
# ll = LinkedList()
# # Insert a node
# ll.insert(4)
# ll.insert(5)
#
# # to list for printing
# print(ll.tolist())
