
class MyQueue:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.front = 0
        self.rear = 0
        self.length = 0

    def enqueue(self, item):
        if self.length == self.size:
            print("Queue is full")
            return
        self.data[self.rear] = item
        self.rear = (self.rear + 1) % self.size
        self.length += 1

    def peek(self):
        if self.length == 0:
            print("Queue is empty")
            return None
        return self.data[self.front]

    def reverseQueue(self):
        reversed_queue = MyQueue(self.size)
        for i in range(self.length):
            index = (self.front + self.length - 1 - i) % self.size
            reversed_queue.enqueue(self.data[index])
        return reversed_queue

    def display(self):
        items = []
        for i in range(self.length):
            index = (self.front + i) % self.size
            items.append(self.data[index])
        return items


size = int(input("Enter the size of the queue: "))
q = MyQueue(size)

for i in range(size):
    value = int(input(f"Enter element {i + 1}: "))
    q.enqueue(value)

print("Original queue:", q.display())
print("Peek:", q.peek())

reversed_q = q.reverseQueue()
print("Reversed queue:", reversed_q.display())