class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_tail(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data


ll2 = LinkedList()

ll2.insert_at_tail(1)
ll2.insert_at_tail(2)
ll2.insert_at_tail(3)
ll2.insert_at_tail(4)
ll2.insert_at_tail(5)

print("Middle:", ll2.find_middle())