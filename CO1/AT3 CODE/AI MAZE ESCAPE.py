from collections import deque
maze = [
    [0,0,0],
    [1,1,0],
    [0,0,0]
]
start = (0,0)
goal = (2,2)
rows = len(maze)
cols = len(maze[0])
queue = deque([(start,[start])])
visited = set()
while queue:
    (x,y),path = queue.popleft()
    if (x,y)==goal:
        print("Shortest Path:")
        print(path)
        break
    if (x,y) in visited:
        continue
    visited.add((x,y))
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx=x+dx
        ny=y+dy
        if 0<=nx<rows and 0<=ny<cols:
            if maze[nx][ny]==0 and (nx,ny) not in visited:
                queue.append(((nx,ny),path+[(nx,ny)]))
