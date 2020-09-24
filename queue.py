# Implementation of Queue data structure using a list object    
class Queue:
    def __init__(self):
        self.queue = []
            
    def enqueue(self, data):
        self.queue.insert(0, data)
        
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop()
    
    def is_empty(self):
        return self.queue == []
    
    def front(self):
        if not self.is_empty():
            return self.queue[-1]
    
    def rear(self):
        if not self.is_empty():
            return self.queue[0]
    
    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.queue)
        
    def get_queue(self):
        return self.queue