class Stack:
    def __init__(self, capacity):
        """Initialize the stack with a fixed capacity (like a C++ array)."""
        self.capacity = capacity  # Fixed size (like array size in C++)
        self.stack = [None] * capacity  # Pre-allocate space
        self.top_index = -1  
    
    def top(self):
        if self.top_index!=-1:
            x = self.stack[self.top_index]
            return x
        raise IndexError("Stack is empty")
    
    def push(self,x):
        if self.top_index+1 < self.capacity:
            self.stack[self.top_index+1] = x 
            self.top_index+=1 
        else:
            raise OverflowError("Stack Overflow: Cannot push, stack is full")
        
    def pop(self):
        if self.top_index>-1:
            x = self.stack[self.top_index]
            del self.stack[self.top_index]
            self.top_index-=1 
            return x
        else:
            raise IndexError("Stack Underflow: Cannot pop, stack is empty")
    
    def is_empty(self):
        return self.top_index==-1 

    def size(self):
        return self.top_index + 1

s= Stack(10)
s.push(10)
s.push(20)
s.push(30)

print("Top element:", s.top())  # Output: 30
print("Stack size:", s.size())  # Output: 3

while not s.is_empty():
    print(s.pop())


