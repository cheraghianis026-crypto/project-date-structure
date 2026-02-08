def peek(self):
    if self.is_empty():
        return None
    return self.queue[self.front]

def is_empty(self):
    return self.front == -1

def reverse(self):
    if self.is_empty() or self.front == self.rear :
        return
    left = self.front
    right = self.rear

    while left < right :
        self.queue[left] , self.queue[right] = self.queue[right] , self.queue[left]
        left +=1
        right -=1
