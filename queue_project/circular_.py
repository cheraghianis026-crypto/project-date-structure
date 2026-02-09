class TestCircularQueue:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.front = 0
        self.rear = 0
        self.length = 0

    def IsEmpty(self):
        return self.length == 0

    def IsFull(self):
        return self.length == self.size

    def enqueue(self, item):
        if self.IsFull():
            print("Queue is full")
            return
        self.data[self.rear] = item
        self.rear = (self.rear + 1) % self.size
        self.length += 1

    def dequeue(self):
        if self.IsEmpty():
            print("Queue is empty")
            return None
        item = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.size
        self.length -= 1
        return item

    def peek(self):
        if self.IsEmpty():
            print("Queue is empty")
            return None
        return self.data[self.front]

    def display(self):
        items = []
        for i in range(self.length):
            index = (self.front + i) % self.size
            items.append(self.data[index])
        return items


# -------- برنامه اصلی ---------

size = int(input("Enter the size of the circular queue: "))
cq = TestCircularQueue(size)

while True:
    print("\nCurrent queue:", cq.display())
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Check if Empty")
    print("5. Check if Full")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        if cq.IsFull():
            print("Queue is full, cannot enqueue.")
        else:
            value = int(input("Enter value to enqueue: "))
            cq.enqueue(value)

    elif choice == '2':
        val = cq.dequeue()
        if val is not None:
            print("Dequeued:", val)

    elif choice == '3':
        val = cq.peek()
        if val is not None:
            print("Front element:", val)

    elif choice == '4':
        print("Queue is empty:", cq.IsEmpty())

    elif choice == '5':
        print("Queue is full:", cq.IsFull())

    elif choice == '6':
        print("Program finished.")
        break

    else:
        print("Invalid choice. Try again.")