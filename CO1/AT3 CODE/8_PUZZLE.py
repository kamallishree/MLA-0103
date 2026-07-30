from queue import PriorityQueue
goal=((1,2,3),
      (4,5,6),
      (7,8,0))
start=((1,2,3),
       (4,0,6),
       (7,5,8))
pq=PriorityQueue()
pq.put((0,start))
visited=set()
while not pq.empty():
    cost,state=pq.get()
    if state==goal:
        print("Solved")
        break
    if state in visited:
        continue
    visited.add(state)
    print(state)
