class Stack :
    def __init__(self):
        self.items = []


def peek(self):
    if not self.is_empty():
        return self.items[-1]
    else:
        raise IndexError("stack is empty")

def is_empty(self):
    return self.top == -1
