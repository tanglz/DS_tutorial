# A balanced tree is a tree in which difference between heights of sub-trees of any node in the tree is not greater than one.
# https://algorithms.tutorialhorizon.com/find-whether-if-a-given-binary-tree-is-balanced/
# binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)

root.right.left = Node(5)
root.right.right = Node(6)

root.right.left.left = Node(7)
root.right.left.right = Node(8)


# root.right.left.left.left = Node(9)

def getHeight(root):
    if root is None:
        return 0
    h_l = getHeight(root.left)
    h_r = getHeight(root.right)
    return 1 + max(h_l, h_r)

print(getHeight(root))

# for each node of the tree,
# get the height of left subtree and right subtree and check the difference ,
# if it is greater than 1, return false.
def is_balanced(root):
    if root is None:
        return True
    height_difference = getHeight(root.left) - getHeight(root.right)
    if abs(height_difference) > 1:
        return False
    else:
        return is_balanced(root.left) and is_balanced(root.right)


print(is_balanced(root))


# better sulution
def get_diff(root):
    if root is None:
        return 0
    h_l = get_diff(root.left)
    if h_l == -1:
        return -1
    h_r = get_diff(root.right)
    if h_r == -1:
        return -1
    diff = h_r - h_l
    if abs(diff > 1):
        return -1
    return 1 + max(h_l, h_r)


def check_balance(root):
    res = get_diff(root)
    if res > 0:
        return True
    else:
        return False

print(check_balance(root))