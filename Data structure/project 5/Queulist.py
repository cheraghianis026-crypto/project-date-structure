class Node:
    def init(self, data):
        self.data = data
        self.next = None
        
        
class CircularQueue:
    def init(self):
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def Enqueue(self, data):
        new_node = Node(data)

        if self.isEmpty():
            self.front = self.rear = new_node
            new_node.next = new_node
        else:
            new_node.next = self.front
            self.rear.next = new_node
            self.rear = new_node

        self.size += 1

    def Dequeue(self):
        if self.isEmpty():
            return None

        removed_data = self.front.data

        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear.next = self.front.next
            self.front = self.front.next

        self.size -= 1
        return removed_data

    def Peek(self):
        if self.isEmpty():
            return None
        return self.front.data

