
class Node:
    def __init__(self , data = None):
        self.data=data
        self.next = self
class Cll:
    def __init__(self):
        self.head = None
        self.count = 0

def InsertAtBegin(self,data):
    new_node = Node(data)

    if self.head is None:
        self.head = new_node
        new_node.next = self.head 
    else :
        t = self.head
        while t.next != self.head :
            t=t.next
        new_node.next=self.head
        t.next = new_node
        self.head = new_node



def InserAtEnd (self , data):
    if self.head is None :
        self.InserAtBegin(data)
        return
    new_node = Node(data)
    t = self.head

    while t.next != self.head:
        t=t.next 
    t.next = new_node
    new_node.next = self.head


def InserAtIndex(self,data,index):
    if index == 0 :
        self.InserAtBegin(data)
        return
    if index == self.size:
        self.InserAtEnd(data)
        return
    
    new_node = Node(data)
    t = self.head
    count = 0

    for _ in range(index -1):
        t = t.next
        count +=1
    new_node.next = t.next
    t.next = new_node


def UpdateNode(self , old_data , new_data):
    if not self.head :
        return
    t = self.head 
    while True :
      if t.data = data :
          t.data = new_data
          return
      t = t.next
      if t == self.head :
          beark

def RemoveNodeBegin (self):
   
    if not self.head :
        return
    if self.head.next == self.head :
        self.head = None
    else:
        t = self.head 
        while t.next != self.head:
            t = t.next 
        t.head = self.head.next 
        self.head= self.head.next
    return removed_data

def RemoveNodeAtEnd(self):
    if not self.head :
        return
    if self.head.next == self.head :
        self.head = None
    else :
    t = self.head
    while t.next.next != self.head:
        t = t.next 
    removed_data = t.next.data
    t.next = self.head
    self.size -=1
    return removed_data

def RemoveNodeAtIndex(self,index):
     if index == 0:
         return self.RemoveNodeBegin()
     if index == self.size-1 :
         return RemoveNodeAtEnd()
     t= self.head
     for _ in range (index-1):
         t=t.next
     removed_data = t.next.data
     t.next = t.next.next 
     self.size -=1
     return removed_data

def Concatenate(self,B):
    if self.head is None:
        self.head = B.head
        self.size = B.size
        return
    if B.head is None:
        return

    n1 = self.head
    while n1.next != self.head :
        n1=n1.next 
    n2 = B.head
    while n2.next != B.head:
        n2=n2.next

    n1.next = B.head
    n2.next = self.head

    self.size += B.size

def  Invert(self):
    if self.head is None or self.head.next == self.head:
        return
    p = None
    c = self.head
    first = self.head
    while True :
        next_node = c.next
        p = c
        c = next_node
        if c == self.head :
         break 
    first.next = p
    self.head = p










 

    



