class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def find_max(node):
    if node is None:
        return float("-inf")  

    left_max = find_max(node.left)
    right_max = find_max(node.right)
    return max(node.value, left_max, right_max)
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
print("Maximum value:", find_max(root))