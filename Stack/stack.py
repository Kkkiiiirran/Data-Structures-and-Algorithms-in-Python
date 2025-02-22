class Stack:
    def __init__(self):
        self.stack = []
    
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
    
    def push(self, x):
        self.stack.append(x)
 

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def is_empty(self):

        return len(self.stack) == 0
s1 = Stack()
s1.push(10)
print(s1.top())

while not s1.is_empty():
    print(s1.pop())


        