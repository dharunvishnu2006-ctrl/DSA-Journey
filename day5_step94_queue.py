from collections import deque    
class Queue:
    def __init__(self):
        self.queue = deque()         

    def enqueue(self, item):
        self.queue.append(item)     

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft() 
        return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.queue[0]     

    def is_empty(self):
        return len(self.queue) == 0  

    def size(self):
        return len(self.queue)      

q = Queue()
q.enqueue(10)     
q.enqueue(20)        
q.enqueue(30)        
print(q.peek())      
print(q.dequeue())   
print(q.peek())     

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity         
        self.queue = [None] * capacity   
        self.front = 0                    
        self.rear = -1                    
        self.size = 0                    

    def enqueue(self, item):
        if self.size == self.capacity:   
            return "Queue is full"
        self.rear = (self.rear + 1) % self.capacity  
        self.queue[self.rear] = item    
        self.size += 1                 

    def dequeue(self):
        if self.size == 0:              
            return "Queue is empty"
        item = self.queue[self.front]    
        self.front = (self.front + 1) % self.capacity 
        self.size -= 1                    
        return item

    def peek(self):
        if self.size == 0:
            return "Queue is empty"
        return self.queue[self.front]     

    def is_full(self):
        return self.size == self.capacity 

    def is_empty(self):
        return self.size == 0           

cq = CircularQueue(3)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
print(cq.is_full())    
print(cq.dequeue())    
cq.enqueue(40)         
print(cq.peek())       

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []   
        self.stack2 = []    
    def enqueue(self, item):
        self.stack1.append(item)    

    def dequeue(self):
        if not self.stack2:                     
            while self.stack1:                  
                self.stack2.append(self.stack1.pop())
        if not self.stack2:                    
            return "Queue is empty"
        return self.stack2.pop()                

    def peek(self):
        if not self.stack2:                      
            while self.stack1:                   
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return "Queue is empty"
        return self.stack2[-1]                 
    def is_empty(self):
        return not self.stack1 and not self.stack2 

qs = QueueUsingStacks()
qs.enqueue(10)
qs.enqueue(20)
qs.enqueue(30)
print(qs.dequeue())  
print(qs.peek())      
print(qs.dequeue())   