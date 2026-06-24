class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None      

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None      

    def insert_at_head(self, data):
        new_node = Node(data)
        if not self.head:                    
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head            
        self.head.prev = new_node            
        self.head = new_node                 

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.tail:                   
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail            
        self.tail.next = new_node       
        self.tail = new_node                 

    def delete_node(self, node):
     
        if node.prev:
            node.prev.next = node.next       
            self.head = node.next            

        if node.next:
            node.next.prev = node.prev       
        else:
            self.tail = node.prev            

    def display_forward(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Forward:  " + " <-> ".join(elements) + " <-> None")

    def display_backward(self):
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.data))
            current = current.prev
        print("Backward: " + " <-> ".join(elements) + " <-> None")

history = DoublyLinkedList()
history.insert_at_tail("CloudShield Dashboard")
history.insert_at_tail("Threat Analysis")
history.insert_at_tail("Alert Details")
history.insert_at_tail("Agent Status")

print("Browsing History:")
history.display_forward()
history.display_backward()

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}        
        self.head = Node("HEAD")   
        self.tail = Node("TAIL")   
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)          
            self._add_to_front(node)    
            return node.data[1]        
        return -1                      

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])   

        new_node = Node((key, value))        
        self._add_to_front(new_node)         
        self.cache[key] = new_node           

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.data[0]]      

    def display(self):
        elements = []
        current = self.head.next
        while current != self.tail:
            elements.append(str(current.data))
            current = current.next
        print("Cache (Most Recent -> Least Recent):", elements)

print("CloudShield X Threat Cache (capacity=3):")
lru = LRUCache(3)

lru.put("IP_192.168.1.1", "MALICIOUS")
lru.put("IP_10.0.0.1", "SAFE")
lru.put("IP_172.16.0.1", "SUSPICIOUS")
lru.display()

print("Get IP_192.168.1.1:", lru.get("IP_192.168.1.1"))  
lru.display()

lru.put("IP_8.8.8.8", "SAFE")   
lru.display()

class Browser:
    def __init__(self):
        self.history = DoublyLinkedList()
        self.current = None

    def visit(self, page):
        self.history.insert_at_tail(page)
        self.current = self.history.tail
        print(f"Visiting: {page}")

    def back(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            print(f"Back to: {self.current.data}")
        else:
            print("No previous page!")

    def forward(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print(f"Forward to: {self.current.data}")
        else:
            print("No next page!")

    def current_page(self):
        if self.current:
            print(f"Current page: {self.current.data}")

print("Sentinel AI India - Agent Monitor Browser:")
browser = Browser()
browser.visit("Sentinel Dashboard")
browser.visit("CloudShield Alerts")
browser.visit("AutoPilot Models")
browser.visit("Agent Status")

browser.current_page()
browser.back()
browser.back()
browser.forward()
browser.back()
browser.back()
browser.back()    