n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
graph = {}
for i in range(n):
    graph[i] = []
print("Enter the edges:")
for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)    
start = int(input("Enter starting vertex: "))
visited = set()
def dfs(vertex):
    visited.add(vertex)
    print(vertex, end=" ")
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(neighbor)
print("DFS Traversal:")
dfs(start)
