from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()  

    def push(self, x):
        """Push an element onto the stack."""
        self.stack.append(x)

    def pop(self):
        """Remove and return the top element. Returns 'Stack is empty' if no elements exist."""
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def top(self):
        """Return the top element without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.stack)

# Example Usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)

while not s.is_empty():
    print(s.pop())  
