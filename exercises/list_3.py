# 3.9

# Linked list in Lesson 4
from introduction.lesson_4.linked_list import LinkedList

L = LinkedList()
L.insert('A')
L.insert('B')
L.insert('C')
M = LinkedList()
M.insert('D')
M.insert('E')
M.insert('F')

print(L.len())
print(L.get_first().data)
print(L.get_last().data)
print(L.get_index(2))

print(M.len())

v = L.get_last()
v.next_node = M.get_first()
K = L
print(K.tolist())
print(K.len())
print(K.get_index(2).next_node.data)