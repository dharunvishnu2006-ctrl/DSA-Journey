class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def count_nodes_in_range(root, low, high):
    if root is None:
        return 0

    if root.value < low:
        return count_nodes_in_range(root.right, low, high)

    if root.value > high:
        return count_nodes_in_range(root.left, low, high)

    return (
        1
        + count_nodes_in_range(root.left, low, high)
        + count_nodes_in_range(root.right, low, high)
    )
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)
print("Nodes in range (25, 65):", count_nodes_in_range(root, 25, 65))