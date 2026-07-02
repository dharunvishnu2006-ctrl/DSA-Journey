class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
def get_height(node):
    if node is None:
        return 0
    return node.height
def get_balance(node):
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)
def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x
def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

n3 = AVLNode(30)
n2 = AVLNode(20)
n1 = AVLNode(10)
n3.left = n2
n2.left = n1
n3.height = 3
n2.height = 2
n1.height = 1

print("Balance factor of n3 before rotation:", get_balance(n3))
new_root = right_rotate(n3)
print("New root value:", new_root.value)

def insert_avl(node, value):
    if node is None:
        return AVLNode(value)
    if value < node.value:
        node.left = insert_avl(node.left, value)
    else:
        node.right = insert_avl(node.right, value)

    node.height = 1 + max(get_height(node.left), get_height(node.right))
    balance = get_balance(node)

    if balance > 1 and value < node.left.value:
        return right_rotate(node)
    
    if balance < -1 and value > node.right.value:
        return left_rotate(node)
    
    if balance > 1 and value > node.left.value:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    
    if balance < -1 and value < node.right.value:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node
avl_root = None
for v in [10, 20, 30, 40, 50, 25]:
    avl_root = insert_avl(avl_root, v)

def inorder_avl(node):
    if node:
        inorder_avl(node.left)
        print(node.value, end=" ")
        inorder_avl(node.right)

inorder_avl(avl_root)
print("\nRoot after balancing:", avl_root.value)