# 3.23
from introduction.lesson_4.circular_linked_list import CLinkedList, CNode

L = CLinkedList()
M = CLinkedList()
# L.insert(3)
# M.insert(3)
node = CNode(5)
L.insert_node(node)
M.insert_node(node)
node2 = CNode(6)
L.insert_node(node2)
M.insert_node(node2)


def check_same(clink_1, clink_2):
    if clink_1.len() != clink_2.len():
        return False
    flag = True
    for i in range(clink_1.len()):
        p = clink_1.get_index(i)
        q = clink_2.get_index(i)
        if p != q:
            flag = False
            break
    return flag


res = check_same(L, M)
print(res)
