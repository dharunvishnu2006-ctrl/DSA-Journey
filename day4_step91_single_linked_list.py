class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

pipeline = LinkedList()
pipeline.insert_at_tail("Parse Logs")
pipeline.insert_at_tail("Filter IPs")
pipeline.insert_at_tail("Detect Threats")
pipeline.insert_at_tail("Generate Alert")

print("CloudShield X Pipeline:")
pipeline.display()

pipeline.delete_node("Filter IPs")
print("After removing Filter IPs:")
pipeline.display()

pipeline.insert_at_head("Receive Logs")
print("After adding Receive Logs at head:")
pipeline.display()

pipeline2 = LinkedList()
pipeline2.insert_at_tail(1)
pipeline2.insert_at_tail(2)
pipeline2.insert_at_tail(3)
pipeline2.insert_at_tail(4)
pipeline2.insert_at_tail(5)

print("\nBefore reverse:")
pipeline2.display()

pipeline2.reverse()
print("After reverse:")
pipeline2.display()

pipeline3 = LinkedList()
pipeline3.insert_at_tail(1)
pipeline3.insert_at_tail(2)
pipeline3.insert_at_tail(3)
pipeline3.insert_at_tail(4)
pipeline3.insert_at_tail(5)

print("\nMiddle element:", pipeline3.find_middle())