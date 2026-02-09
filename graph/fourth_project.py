class Graph:
    def __init__(self):
        self.vertices = {}

    def AddVertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
            print(f"Vertex '{vertex}' added.")
        else:
            print(f"Vertex '{vertex}' already exists.")

    def AddEdge(self, firstVertex, secondVertex):
        if firstVertex not in self.vertices:
            print(f"Vertex '{firstVertex}' does not exist.")
            return
        if secondVertex not in self.vertices:
            print(f"Vertex '{secondVertex}' does not exist.")
            return
        self.vertices[firstVertex].append(secondVertex)
        # اگر گراف بدون جهت بخواییم، این خط رو از حالت کامنت درمیاریم
        #self.vertices[secondVertex].append(firstVertex)
        print(f"Edge from '{firstVertex}' to '{secondVertex}' added.")

    def Display(self):
        if not self.vertices:
            print("Graph is empty.")
            return
        print("\nGraph adjacency list:")
        for vertex in self.vertices:
            print(f"{vertex} -> {self.vertices[vertex]}")


graph = Graph()

while True:
    print("\nMenu:")
    print("1. Add Vertex")
    print("2. Add Edge")
    print("3. Display Graph")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        v = input("Enter vertex name: ")
        graph.AddVertex(v)

    elif choice == '2':
        v1 = input("Enter first vertex: ")
        v2 = input("Enter second vertex: ")
        graph.AddEdge(v1, v2)

    elif choice == '3':
        graph.Display()

    elif choice == '4':
        print("Program finished.")
        break

    else:
        print("Invalid choice. Try again.")