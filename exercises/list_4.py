# 3.10
from introduction.lesson_4.doubly_linked_list import DLinkedList

L = DLinkedList()
L.insert('A')
L.insert('B')
L.insert('C')
M = DLinkedList()
M.insert('D')
M.insert('E')
M.insert('F')

print(L.len())
print(M.len())

temp_1 = L.get_last()
temp_2 = M.get_first()
temp_1.next_node=temp_2
temp_2.pre_node = temp_1

K = L
print(K.len())
print(K.tolist())
print(K.get_index(2).next_node.data)
print(K.get_index(3).pre_node.data)
print(K.get_first().data)
print(K.get_last().data)