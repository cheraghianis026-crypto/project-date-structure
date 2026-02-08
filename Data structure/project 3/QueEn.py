class Queue :
    def __init__(self,size):
        self.size = size
        self.queue = [None]*size
        self.front = -1
        self.rear = -1
    
    def enqueue(self , value):
       if self.front == self.size -1 :
           print("queue is full")
           return
       self.rear +=1 
       self.queue[self.rear] = value
      
        
          

    def dequeue (self):
        if self.front == -1 or self.front > self.rear :
            print("queue is empty")
        value = self.queu[self.front]
        self.front +=1
        return value

           

