from collections import deque
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
a = int(input("Enter starting vertex: "))
visited = set()
queue = deque()
visited.add(a)
queue.append(a)
print("BFS Traversal:")
while queue:
    vertex = queue.popleft()
    print(vertex, end=" ")
    for nxt in graph[vertex]:
        if nxt not in visited:
            visited.add(nxt)
            queue.append(nxt)
