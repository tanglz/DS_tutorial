# A class to store a binary tree node
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


# Traverse nodes in reverse preorder fashion
def printRightView(root, level, d):
    if root is None:
        return

    # insert the current node and level information into the dictionary
    d[level] = root.key
    # recur for the left subtree before the right subtree
    printRightView(root.left, level + 1, d)
    printRightView(root.right, level + 1, d)


# Function to print the right view of a given binary tree
def printRightViewTree(root):
    # create an empty dictionary to store the last node for each level
    d = {}

    # traverse the tree and fill the dictionary
    printRightView(root, 1, d)

    # iterate through the dictionary in sorted order of its keys and print
    # the right view
    print(list(d.values()))


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    printRightViewTree(root)