class Stack:
    def __init__(self):
        self.stack = []        

    def push(self, item):
        self.stack.append(item)  

    def pop(self):
        if not self.is_empty():
            return self.stack.pop() 
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]    
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0  

    def size(self):
        return len(self.stack)       

s = Stack()
s.push(10)      
s.push(20)    
s.push(30)       
print(s.peek()) 
print(s.pop())   
print(s.peek())  

def valid_parentheses(s):
    stack = []                        

    pairs = {')': '(',                
             '}': '{',
             ']': '['}

    for char in s:                   
        if char in '({[':             
            stack.append(char)     
        elif char in ')}]':           
            if not stack:             
                return False
            if stack[-1] != pairs[char]:  
                return False
            stack.pop()              

    return len(stack) == 0          
print(valid_parentheses("()"))     
print(valid_parentheses("()[]{}"))  
print(valid_parentheses("(]"))      
print(valid_parentheses("([)]"))   
print(valid_parentheses("{[]}"))

class MinStack:
    def __init__(self):
        self.stack = []         
        self.min_stack = []     

    def push(self, val):
        self.stack.append(val)             

        if not self.min_stack:           
            self.min_stack.append(val)       
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()        
        self.min_stack.pop()    
    def top(self):
        return self.stack[-1]   

    def get_min(self):
        return self.min_stack[-1]  
ms = MinStack()
ms.push(5)
ms.push(3)
ms.push(7)
ms.push(2)
print(ms.get_min())   
ms.pop()
print(ms.get_min())   
print(ms.top())       