from collections import deque
capacity1=11
capacity2=9
goal=8
visited=set()
queue=deque()
queue.append((0,0,[]))
while queue:
    x,y,path=queue.popleft()
    if (x,y) in visited:
        continue
    visited.add((x,y))
    if x==goal or y==goal:
        print("Solution")
        for step in path:
            print(step)
        print((x,y))
        break
    next_states=[]
    next_states.append((capacity1,y))
    next_states.append((x,capacity2))
    next_states.append((0,y))
    next_states.append((x,0))
    transfer=min(x,capacity2-y)
    next_states.append((x-transfer,y+transfer))
    transfer=min(y,capacity1-x)
    next_states.append((x+transfer,y-transfer))
    for state in next_states:
        if state not in visited:
            queue.append((state[0],state[1],path+[state]))
