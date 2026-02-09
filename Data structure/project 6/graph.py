class Graph():
    def __init__(self , n):
        self.size = n 
        self.M=[]
        for i in range(n):
            self.M.append([0 for i in range(n)])

def RemoveEdge(self , v1 , v2 ):
    self.M[v1][v2]=0
    self.M[v2][v1]=0

def RemoveVertex(self, v):
    for i in range (self.size):
        self.M[v][i] = 0
        self.M[i][v]=0 
'''
class Graph:
    def init(self):
        self.adj = {}

    def RemoveEdge(self, v1, v2):
        if v1 in self.adj and v2 in self.adj:
            for i in range(len(self.adj[v1])):
                if self.adj[v1][i] == v2:
                    del self.adj[v1][i]
                    break

            for i in range(len(self.adj[v2])):
                if self.adj[v2][i] == v1:
                    del self.adj[v2][i]
                    break

    def RemoveVertex(self, v):
        if v in self.adj:
            for neighbor in self.adj[v]:
                for i in range(len(self.adj[neighbor])):
                    if self.adj[neighbor][i] == v:
                        del self.adj[neighbor][i]
                        break
            del self.adj[v]
   '''




