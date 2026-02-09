class Stack :
    def __init__(self , size):
        self.size = size
        self.stack = [None]*size
        self.top = -1


def peek(self):
    if not self.is_empty():
        return self.stack[self.top]
    else:
        raise IndexError("stack is empty")

def is_empty(self):
    return self.top == -1

