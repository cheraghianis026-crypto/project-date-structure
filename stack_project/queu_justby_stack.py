class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            print("Queue is empty")
            return None
        return self.stack2.pop()

    def display(self):
        result = []
        result.extend(reversed(self.stack2))
        result.extend(self.stack1)
        return result


q = QueueUsingStacks()

while True:
    print("\nCurrent queue:", q.display())
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        value = input("Enter value to enqueue: ")
        q.enqueue(value)
    elif choice == '2':
        val = q.dequeue()
        if val is not None:
            print("Dequeued:", val)
    elif choice == '3':
        print("Program finished.")
        break
    else:
        print("Invalid choice. Try again.")