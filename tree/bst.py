# Binary Search Tree, further reading: https://medium.com/techie-delight/binary-search-tree-bst-practice-problems-and-interview-questions-ea13a6731098
# BST is a type of Binary tree which has a special property.
# Nodes smaller than root goes to the left of the root and Nodes greater than root goes to the right of the root.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    root = None

    def __init__(self, root_key):
        root_node = Node(root_key)
        self.root = root_node

    # add a node to the tree with value data
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            parent = current
            if data < current.data:
                current = current.left
                if current is None:
                    parent.left = new_node
                    break
            else:
                current = current.right
                if current is None:
                    parent.right = new_node
                    break

    # find a node with value data
    def find(self, data):
        current = self.root
        while current:
            if current.data == data:
                return True
            elif current.data>data:
                current = current.left
            else:
                current = current.right
        return False


    def getSuccessor(self, node):
        successor = None
        successor_parent = None
        current = node.right
        while current:
            successor_parent = successor
            successor = current
            current = current.left
        # check if successor has the right child, it cannot have left child for sure
        # is it does have the right child, add it to the left of successorparent.
        if successor is not node.right:
            successor_parent.left = successor.right
            successor.right = node.right
        return successor

    # delete a node with value data
    def delete(self, data):
        parent = self.root
        current = self.root
        is_left_child = False
        while current.data!=data:
            parent = current
            if current.data>data:
                is_left_child = True
                current = current.left
            else:
                is_left_child = False
                current = current.right
            if current is None:
                return False
        # case 1: if node to be deleted has no children
        if current.left is None and current.right is None:
            if current is self.root:
                self.root = None
            if is_left_child:
                parent.left =None
            else:
                parent.right=None
        # case 2: if node to be deleted has only one child
        elif current.right is None:
            if current is self.root:
                self.root=current.left
            elif is_left_child:
                parent.left = current.left
            else:
                parent.right = current.left
        elif current.left is None:
            if current is self.root:
                self.root = current.right
            elif is_left_child:
                parent.left = current.right
            else:
                parent.right = current.right
        # case 3 if node to be deleted has two children
        elif current.left is not None and current.right is not None:
            successor = self.getSuccessor(current)
            if current is self.root:
                self.root = successor
            elif is_left_child:
                parent.left = successor
            else:
                parent.right = successor
            successor.left = current.left
        return True

    # display the entire tree in increasing order
    def display(self, node):
        if self.root is None:
            print("It is empty!")
        if node:
            self.display(node.left)
            print(node.data, end=" ")
            self.display(node.right)



# create a bst instance
bst = BinarySearchTree(3)
# insert
bst.insert(20)
bst.insert(25)
bst.insert(15)
bst.insert(16)
bst.insert(8)
bst.insert(1)
bst.insert(4)
bst.insert(6)
bst.insert(2)
bst.insert(10)
bst.insert(9)
bst.insert(21)

# display
bst.display(bst.root)

# find
print("")
print(bst.find(22), end="\n")

# delete
bst.delete(6)
bst.display(bst.root)