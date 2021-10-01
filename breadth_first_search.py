from collections import defaultdict
 
# This class represents a directed graph
# using adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def add_edge(self,u,v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " --> ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 

# Create a graph given in
# the above diagram
g = Graph()

no_of_edges = int(input("Enter number of edges : "))
for i in range(no_of_edges) : 
    start = int(input("Starting point of edge {} : ".format(i + 1)))
    end = int(input("Ending point of edge {} : ".format(i + 1)))
    g.add_edge(start, end)
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 0)
# g.add_edge(2, 3)
# g.add_edge(3, 3)
first = int(input("Enter starting node for BFS : "))
print ("BFS : ", end = "\n")
g.BFS(first)

"""
Example output : 

Enter number of edges : 6
Starting point of edge 1 : 0
Ending point of edge 1 : 1
Starting point of edge 2 : 0
Ending point of edge 2 : 3
Starting point of edge 3 : 2
Ending point of edge 3 : 0
Starting point of edge 4 : 1
Ending point of edge 4 : 2
Starting point of edge 5 : 2
Ending point of edge 5 : 3
Starting point of edge 6 : 3
Ending point of edge 6 : 2
Enter starting node for BFS : 0
BFS : 
0 --> 1 --> 3 --> 2 -->  
"""