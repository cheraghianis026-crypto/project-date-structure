from typing import dataclass_transform


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

    self.size +=1

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
    self.size +=1

def InserAtIndex(self,data,index):
    if (index > self.size) |(index<0):
        print("Index out of range")
    if index == 0 :
        self.InserAtBegin(data)
        return
    if index == self.size:
        self.InserAtEnd(data)
        return
    
    new_node = Node(data)
    t = self.head

    for _ in range(index -1):
        t = t.next
    new_node.next = t.next
    t.next = new_node
    self.size +=1

def UpdateNode(self , data , index):
    if (index > self.size) |(index<0):
        print("Index out of range")
    t = self.head 
    for _ in range(index):
        t = t.next 
    t.data = data

def RemoveNodeBegin (self):
   
    if self.size == 1 :
        self.head = None
        self.size = 0
    removed_data = self.head.data
    if self.head.next == self.head :
        self.head = None
    else:
        t = self.head 
        while t.next != self.head:
            t = t.next 
        self.head = self.head.next 
        t.next = self.head
    self.size -=1
    return removed_data

def RemoveNodeAtEnd(self):
    if self.size == 1 :
        self.head = None
        self.size = 0
    t = self.head
    while t.next.next != self.head:
        t = t.next 
    removed_data = t.next.data
    t.next = self.head
    self.size -=1
    return removed_data

def RemoveNodeAtIndex(self,index):
     if (index > self.size) |(index<0):
        print("Index out of range")
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
    q = self.head
    t=q.next
    while True :
        next_node = q.next 
        q.next = p
        p = q
        q = next_node
        if q == self.head :
         break 
    self.head.next = p
    self.head = p










 

    


