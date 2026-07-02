class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

root = None
for v in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, v)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

inorder(root)

def search(root, value):
    if root is None:
        return False
    if root.value == value:
        return True
    if value < root.value:
        return search(root.left, value)
    else:
        return search(root.right, value)
print(search(root, 40)) 
print(search(root, 99))           

def is_valid_bst(node, low=float("-inf"), high=float("inf")):
    if node is None:
        return True
    if not (low < node.value < high):
        return False
    return (is_valid_bst(node.left, low, node.value) and
            is_valid_bst(node.right, node.value, high))
print(is_valid_bst(root))