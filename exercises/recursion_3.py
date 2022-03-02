# 3-15
from introduction.lesson_4.linked_list import LinkedList


def count_nodes(slist, node):
    if node is None:
        return 0
    return count_nodes(slist,node.next_node)+1

s = LinkedList()
s.insert(3)
s.insert(4)
s.insert(5)
s.insert(6)
s.insert(7)
print(s.tolist())

cnt = count_nodes(s,s.head)
print(cnt)