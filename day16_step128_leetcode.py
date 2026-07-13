class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      
        self.next = next    

def reverseList(head):
    prev = None             
    curr = head               
    while curr:
        next_node = curr.next   
        curr.next = prev        
        prev = curr            
        curr = next_node        
    return prev               

n3 = ListNode(3)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

new_head = reverseList(n1)
curr = new_head
while curr:
    print(curr.val, end=" ")
    curr = curr.next

def hasCycle(head):
    slow = head              
    fast = head               

    while fast and fast.next:
        slow = slow.next            
        fast = fast.next.next       

        if slow == fast:
            return True             

    return False                        

n3 = ListNode(3)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
n3.next = n2  
print(hasCycle(n1))   

m3 = ListNode(3)
m2 = ListNode(2, m3)
m1 = ListNode(1, m2)

print(hasCycle(m1))

def getIntersectionNode(headA, headB):
    pA = headA                  
    pB = headB         
    while pA != pB:
        pA = pA.next if pA else headB   
        pB = pB.next if pB else headA   
    return pA               

shared = ListNode(8, ListNode(4, ListNode(5)))
headA = ListNode(4, ListNode(1, shared))
headB = ListNode(5, ListNode(6, ListNode(1, shared)))
result = getIntersectionNode(headA, headB)
print(result.val)

def isPalindrome(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    left = head
    right = prev              
    while right:               
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True

n4 = ListNode(1)
n3 = ListNode(2, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
print(isPalindrome(n1))   

m3 = ListNode(3)
m2 = ListNode(2, m3)
m1 = ListNode(1, m2)
print(isPalindrome(m1))   
