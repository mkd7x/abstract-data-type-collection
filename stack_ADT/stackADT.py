class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.size = 0
    
    def push(self, newItem):
        self.stack.append(newItem)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.stack.pop(-1)
        else:
            return None

    def top(self):
        if self.size > 0:
            return self.stack[-1]
        else:
            return None

    def size(self):
        return self.size

    def isEmptyStack(self):
        if self.size == 0:
            return True
        else:
            return False
