class Node:
    def __init__(self, v):
        self.v, self.l, self.r = v, None, None

def insert(n, v):
    if not n: return Node(v)
    if v < n.v: n.l = insert(n.l, v)
    else: n.r = insert(n.r, v)

    if n.l and n.l.l:
        return right_rotate(n)
    return n

def right_rotate(y):
    x = y.l
    y.l = x.r
    x.r = y
    return x

def inorder(n):
    return inorder(n.l)+[n.v]+inorder(n.r) if n else []
root = None
for v in [10, 5, 1]:
    root = insert(root, v)
print(inorder(root))
print(root.v)