class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

middle = middleNode(n1)
print("Middle node value:", middle.val)  

m4 = ListNode(4)
m3 = ListNode(3, m4)
m2 = ListNode(2, m3)
m1 = ListNode(1, m2)

middle = middleNode(m1)
print("Middle node value:", middle.val)