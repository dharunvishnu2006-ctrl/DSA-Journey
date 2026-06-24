class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(key=data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(key=data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display_forward(self):
        current = self.head
        result = "Forward: "
        while current:
            result += str(current.key) + " <-> "
            current = current.next
        result += "None"
        print(result)

    def display_backward(self):
        current = self.tail
        result = "Backward: "
        while current:
            result += str(current.key) + " <-> "
            current = current.prev
        result += "None"
        print(result)

dll = DoublyLinkedList()
dll.insert_at_tail("CloudShield")
dll.insert_at_tail("AutoPilot")
dll.insert_at_head("Sentinel")
dll.display_forward()
dll.display_backward()

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return None
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
            return
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_front(new_node)
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]

    def display(self):
        current = self.head.next
        result = []
        while current != self.tail:
            result.append(f"{current.key}:{current.value}")
            current = current.next
        print("LRU Order:", " <-> ".join(result))

lru = LRUCache(3)
lru.put("IP1", "MALICIOUS")
lru.put("IP2", "SAFE")
lru.put("IP3", "SUSPICIOUS")
lru.display()

lru.get("IP1")
lru.display()

lru.put("IP4", "SAFE")
lru.display()