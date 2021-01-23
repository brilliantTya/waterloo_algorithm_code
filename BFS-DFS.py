class Stack:
    def __init__(self, arr=None):
        if arr is None:
            self.arr = []
        else:
            self.arr = arr

    def push(self, obj):
        self.arr.append(obj)

    def pop(self):
        return self.arr.pop()

    def isEmpty(self):
        return len(self.arr) == 0


class Queue:
    def __init__(self, arr=None):
        if arr is None:
            self.arr = []
        else:
            self.arr = arr

    def push(self, obj):
        self.arr.append(obj)

    def pop(self):
        return self.arr.pop(0)

    def isEmpty(self):
        return len(self.arr) == 0


class Vertex:
    def __init__(self, value, neighbors=[]):
        self.value = value
        self.neighbors = neighbors

    def __repr__(self):
        return str(self.value)


class BFS:
    def __init__(self, vertices, directed=False):
        self.directed = directed
        self.vertices = vertices

        self.resetConnection()
        self.connected = self.checkConnectivity()
        self.bipartiteness = self.bipartite()

    def resetConnection(self):
        for vertex in self.vertices:
            vertex.visited = False
            vertex.distance = float('inf')

    def connect(self, root):
        self.resetConnection()
        distance = 0
        root.visited = True
        root.distance = 0
        queue = Queue()
        queue.push(root)

        while not queue.isEmpty():
            curr = queue.pop()
            for neighbor in curr.neighbors:
                if not neighbor.visited:
                    neighbor.visited = True
                    neighbor.distance = curr.distance + 1
                    queue.push(neighbor)

    def checkConnectivity(self):
        self.connect(self.vertices[0])
        for vertex in self.vertices:
            if not vertex.visited:
                return False
        return True

    def shortestDistance(self, vertex1, vertex2):
        self.resetConnection()
        self.connect(vertex1)
        return vertex2.distance

    def bipartite(self):
        self.resetConnection()
        self.connect(self.vertices[0])
        even, odd = [], []
        for vertex in self.vertices:
            if vertex.visited and vertex.distance % 2 == 0:
                even.append(vertex)
            elif vertex.visited and vertex.distance % 2 == 1:
                odd.append(vertex)
        for vertex in even:
            for neighbor in vertex.neighbors:
                if neighbor in even:
                    return False
        for vertex in odd:
            for neighbor in vertex.neighbors:
                if neighbor in odd:
                    return False
        return True


class DFS:
    def __init__(self, vertices, directed=False):
        self.directed = directed
        self.vertices = vertices

        self.resetConnection()
        self.connectivity = self.checkConnectivity()

    def resetConnection(self):
        for vertex in self.vertices:
            vertex.visited = False
            vertex.start, vertex.end = float('inf'), float('inf')

    def connect(self, root):
        self.resetConnection()
        stack = Stack()
        stack.push(root)
        root.visited = True
        root.start = time

        while not stack.isEmpty():
            curr = stack.pop()
            for neighbor in curr.neighbors:
                if not neighbor.visited:
                    neighbor.visited = True
                    neighbor.start = time
                    stack.push(neighbor)

    def checkConnectivity(self):
        self.connect(self.vertices[0])
        for vertex in self.vertices:
            if not vertex.visited:
                return False
        return True


if __name__ == '__main__':
    a, b, c, d, e, f = Vertex('a'), Vertex('b'), \
        Vertex('c'), Vertex('d'), Vertex('e'), Vertex('f')
    a.neighbors = [d, e, f]
    b.neighbors = [e, f]
    c.neighbors = [d, f]
    d.neighbors = [a, c]
    e.neighbors = [a, b]
    f.neighbors = [a, b, c]
    ds = DFS([a, b, c, d, e, f])
    print(ds.connectivity)
