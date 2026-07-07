def range_min_query(arr):
    n = len(arr)
    tree = [0] * (4 * n)

    def build(node, start, end):
        if start == end:
            tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = min(tree[2 * node], tree[2 * node + 1])

    def query(node, start, end, left, right):
        if right < start or end < left:
            return float('inf')
        if left <= start and end <= right:
            return tree[node]

        mid = (start + end) // 2
        return min(
            query(2 * node, start, mid, left, right),
            query(2 * node + 1, mid + 1, end, left, right)
        )

    build(1, 0, n - 1)
    return lambda l, r: query(1, 0, n - 1, l, r)
arr = [5, 2, 6, 3, 1, 7]
rmq = range_min_query(arr)
print(rmq(1, 4))