from binarytree import Node

from collections import deque

# This class represents a directed graph using adjacency list representation


class Graph:
    def __init__(self, V):
        self.V = V  # No. of vertices
        self.adj = [[] for _ in range(V)]  # Adjacency lists

    # Function to add an edge to graph
    def addEdge(self, v, w):
        self.adj[v].append(w)  # Add w to v’s list

    # Prints BFS traversal from a given source s
    def BFS(self, s):
        # Mark all the vertices as not visited
        visited = [False] * self.V

        # Create a queue for BFS
        queue = deque()

        # Mark the current node as visited and enqueue it
        visited[s] = True
        queue.append(s)

        # Create a mapping from integers to characters
        mapping = ['A', 'B', 'C', 'D', 'E', 'F']

        while queue:
            # Dequeue a vertex from queue and print it
            s = queue.popleft()
            # Use the mapping to print the original label
            print(mapping[s], end=" ")

            # Get all adjacent vertices of the dequeued vertex s
            # If an adjacent has not been visited, then mark it visited
            # and enqueue it
            for i in self.adj[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


if __name__ == "__main__":
    # Create a graph given in the diagram
    #      A
    #     / \
    #    B   C
    #   /   / \
    #  D   E   F
    g = Graph(6)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(2, 5)

    print("Breadth First Traversal is: ", end="")
    g.BFS(0)  # Start BFS from A (0)


root = Node(3)
root.left = Node(32)
root.right = Node(1)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(5)
root.right.left = Node(6)


print(root)



print(root.postorder)
from binarytree import Node

# Create the binary tree
root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(2)

def bfs(node):
    if not node:
        return []

    queue = [node]  # Initialize the queue with the root node
    result = []

    while queue:
        current = queue.pop(0)  # Dequeue the front node
        result.append(current.value)  # Process the current node

        # Enqueue left and right children if they exist
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result

# Print the binary tree structure
print("Binary Tree Structure:\n", root)

# Perform BFS and print the result
print("BFS Traversal:",bfs(root))





from binarytree import Node

# Create the binary tree
root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(2)
root.right.left = Node(4)
root.right.right = Node(3)
def bfs(node):

    queue = [node]  # Initialize the queue with the root node
    result = []

    while queue:
        current = queue.pop(0)  # Dequeue the front node
        result.append(current.value)  # Process the current node

        # Enqueue left and right children if they exist
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result

# Print the binary tree structure
print("Binary Tree Structure:\n", root)
print(root.levelorder)

# Perform BFS and print the result
print("BFS Traversal:",bfs(root))
from binarytree import Node

from collections import deque

# This class represents a directed graph using adjacency list representation


class Graph:
    def __init__(self, V):
        self.V = V  # No. of vertices
        self.adj = [[] for _ in range(V)]  # Adjacency lists

    # Function to add an edge to graph
    def addEdge(self, v, w):
        self.adj[v].append(w)  # Add w to v’s list

    # Prints BFS traversal from a given source s
    def BFS(self, s):
        # Mark all the vertices as not visited
        visited = [False] * self.V

        # Create a queue for BFS
        queue = deque()

        # Mark the current node as visited and enqueue it
        visited[s] = True
        queue.append(s)

        # Create a mapping from integers to characters
        mapping = ['A', 'B', 'C', 'D', 'E', 'F']

        while queue:
            # Dequeue a vertex from queue and print it
            s = queue.popleft()
            # Use the mapping to print the original label
            print(mapping[s], end=" ")

            # Get all adjacent vertices of the dequeued vertex s
            # If an adjacent has not been visited, then mark it visited
            # and enqueue it
            for i in self.adj[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


if __name__ == "__main__":
    # Create a graph given in the diagram
    #      A
    #     / \
    #    B   C
    #   /   / \
    #  D   E   F
    g = Graph(6)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(2, 5)

    print("Breadth First Traversal is: ", end="")
    g.BFS(0)  # Start BFS from A (0)


root = Node(3)
root.left = Node(32)
root.right = Node(1)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(5)
root.right.left = Node(6)


print(root)



print(root.postorder)
from binarytree import Node

# Create the binary tree
root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(2)

def bfs(node):
    if not node:
        return []

    queue = [node]  # Initialize the queue with the root node
    result = []

    while queue:
        current = queue.pop(0)  # Dequeue the front node
        result.append(current.value)  # Process the current node

        # Enqueue left and right children if they exist
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result

# Print the binary tree structure
print("Binary Tree Structure:\n", root)

# Perform BFS and print the result
print("BFS Traversal:",bfs(root))





from binarytree import Node

# Create the binary tree
root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(2)
root.right.left = Node(4)
root.right.right = Node(3)
def bfs(node):

    queue = [node]  # Initialize the queue with the root node
    result = []

    while queue:
        current = queue.pop(0)  # Dequeue the front node
        result.append(current.value)  # Process the current node

        # Enqueue left and right children if they exist
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result

# Print the binary tree structure
print("Binary Tree Structure:\n", root)
print(root.levelorder)

# Perform BFS and print the result
print("BFS Traversal:",bfs(root))
