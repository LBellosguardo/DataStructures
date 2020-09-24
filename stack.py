# Implementation of Stack data structure using a list object
class Stack:
    
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        return self.stack.pop()
    
    def is_empty(self):
        return self.stack == []
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty!")
            
    def size(self):
        return len(self.stack)
    
    def __len__(self):
        return self.size()
    
    def get_stack(self):
        return self.stack