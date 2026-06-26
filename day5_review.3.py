from collections import deque

def hot_potato(names, num):
    queue = deque(names)

    while len(queue) > 1:
        for _ in range(num):
            queue.append(queue.popleft())
        queue.popleft()

    return queue[0]

players = ["Alice", "Bob", "Charlie", "Diana"]
print(hot_potato(players, 3))