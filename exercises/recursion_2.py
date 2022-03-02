# 3-8
from introduction.lesson_4.linked_list import LinkedList


# Method to reverse the list
def reverse(slist, node):
    # If head is empty or has reached the list end
    if node is None or node.next_node is None:
        return node
    # Reverse the rest list
    rest = reverse(slist, node.next_node)
    # Put first element at the end
    node.next_node.next_node = node
    node.next_node = None
    # Fix the header pointer
    return rest


s = LinkedList()
s.insert(3)
s.insert(4)
s.insert(5)
s.insert(6)
s.insert(8)
print(s.tolist())
s.head = reverse(s, s.head)
print(s.tolist())
