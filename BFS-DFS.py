class Stack:
    def __init__(self, arr=None):
        if arr is None:
            self.arr = []
        else:
            self.arr = arr

    def push(self, obj):
        self.arr.append(obj)

    def pop(self):
        if not self.is_empty():
            return self.arr.pop()
        else:
            raise IndexError

    def peek(self):
        if not self.is_empty():
            return self.arr[-1]
        else:
            raise IndexError

    def is_empty(self):
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
        if not self.is_empty():
            return self.arr.pop(0)
        else:
            raise IndexError

    def is_empty(self):
        return len(self.arr) == 0


class Vertex:
    def __init__(self, value, neighbors=None):
        self.value = value
        self.neighbors = neighbors

    def __repr__(self):
        return str(self.value)


class BFS:
    def __init__(self, vertices, directed=False):
        self.directed = directed
        self.vertices = vertices

        self.reset_connection()
        self.connected = self.check_connectivity()
        self.bipartiteness = self.bipartite()

    def reset_connection(self):
        for vertex in self.vertices:
            vertex.visited = False
            vertex.distance = float('inf')

    def connect(self, root):
        self.reset_connection()
        root.visited = True
        root.distance = 0
        queue = Queue()
        queue.push(root)

        while not queue.is_empty():
            curr = queue.pop()
            for neighbor in curr.neighbors:
                if not neighbor.visited:
                    neighbor.visited = True
                    neighbor.distance = curr.distance + 1
                    queue.push(neighbor)

    def check_connectivity(self):
        self.connect(self.vertices[0])
        for vertex in self.vertices:
            if not vertex.visited:
                return False
        return True

    def shortest_distance(self, vertex1, vertex2):
        self.reset_connection()
        self.connect(vertex1)
        return vertex2.distance

    def bipartite(self):
        self.reset_connection()
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

        self.reset_connection()
        self.connectivity = self.check_connectivity()

    def reset_connection(self):
        for vertex in self.vertices:
            vertex.visited = False
            vertex.start, vertex.end = float('inf'), float('inf')

    def connect(self, root):
        self.reset_connection()
        stack = Stack()
        stack.push(root)
        root.visited = True

        while not stack.is_empty():
            curr = stack.peek()
            finished = True
            for neighbor in curr.neighbors:
                if not neighbor.visited:
                    neighbor.visited = True
                    stack.push(neighbor)
                    finished = False
                    break
            if finished:
                stack.pop()

    def check_connectivity(self):
        self.connect(self.vertices[0])
        for vertex in self.vertices:
            if not vertex.visited:
                return False
        return True


if __name__ == '__main__':
    a, b, c, d, e, f = Vertex('a'), Vertex('b'), \
        Vertex('c'), Vertex('d'), Vertex('e'), Vertex('f')
    a.neighbors = [d, e]
    b.neighbors = [e]
    c.neighbors = [d]
    d.neighbors = [a, c]
    e.neighbors = [a, b]
    ds = DFS([a, b, c, d, e, f])
    print(ds.connectivity)
