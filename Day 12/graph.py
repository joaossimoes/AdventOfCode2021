from collections import defaultdict
from os import truncate
  
# This class represents a directed graph
# using adjacency list representation
class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices
         
        # default dictionary to store graph
        self.graph = defaultdict(list)

    def __str__(self):
        return list(self.graph)
    
    def __repr__(self) -> str:
        return str(self.graph)
  
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)



        # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d, vertices):
 
        # Mark all the vertices as not visited
        visited = {}
        howVisited = {}
        for vertice in vertices:
            visited[vertice] = False
            howVisited[vertice] = 0
        # Create an array to store paths
        path = []
        flag = False
        # Call the recursive helper function to print all paths
        
        return self.printAllPathsUtil(s, d, visited, path, flag, howVisited)


    
    def printAllPathsUtil(self, u, d, visited, path, flag, howVisited):
        paths = []
        # Mark the current node as visited and store in path
        
        if u.isupper():
            visited[u] = False
            howVisited[u] += 1
        else:
            visited[u] = True
            howVisited[u] += 1
            if howVisited[u] > 1:
                flag = True
                
        path.append(u)
        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            # print(path)
            # print(howVisited, flag)
            # print(visited)
            paths.append(path[:])
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                    if visited[i] == False or (i.islower and not flag and i != "start"):
                        paths.extend(self.printAllPathsUtil(i, d, visited, path, flag, howVisited))
                    
        # Remove current vertex from path[] and mark it as unvisited
        # print(howVisited, flag)
        # print(path)
        path.pop()
        howVisited[u] -= 1
        if u.isupper() or (u.islower and howVisited[u] == 0):
            visited[u]= False
        else:
            visited[u] = True
        
        return paths