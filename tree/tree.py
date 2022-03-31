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

# tree traversals recursive approach, non-recursive approaches are implemented with stack
# # Inorder left->root_>right https://www.techiedelight.com/inorder-tree-traversal-iterative-recursive/
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)


# # Preorder root->left->right https://www.techiedelight.com/preorder-tree-traversal-iterative-recursive/
def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)


# # Postorder left->right->root https://www.techiedelight.com/postorder-tree-traversal-iterative-recursive/
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')

print('inorder:', end=' ')
inorder(root)
print('\n')
print('preorder:', end=' ')
preorder(root)
print('\n')
print('postorder', end=' ')
postorder(root)