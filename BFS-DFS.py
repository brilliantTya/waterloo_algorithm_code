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

        for vertex in self.vertices:
            vertex.visited = False
            vertex.distance = float('inf')
        self.connected = self.checkConnectivity(self.vertices[0])

    def checkConnectivity(self, root):
        distance = 0
        root.visited = True
        root.distance = 0
        stack = Stack()
        stack.push(root)

        while not stack.isEmpty():
            curr = stack.pop()
            distance += 1
            for neighbor in curr.neighbors:
                if not neighbor.visited:
                    neighbor.visited = True
                    neighbor.distance = distance
                    stack.push(neighbor)

        for vertex in self.vertices:
            if not vertex.visited:
                return False
        return True


if __name__ == '__main__':
    a, b, c, d, e, f = Vertex('a'), Vertex('b'), \
        Vertex('c'), Vertex('d'), Vertex('e'), Vertex('f')
    a.neighbors = [b, c]
    b.neighbors = [a, c, d]
    c.neighbors = [a, b, e]
    d.neighbors = [b, e]
    e.neighbors = [c, d]
    ds = BFS([a, b, c, d, e])
    print(ds.connected)
