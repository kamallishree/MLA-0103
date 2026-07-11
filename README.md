## BFS PSEUDO CODE ##
BFS(Graph, Start)
Create an empty queue
Create an empty visited set
Mark Start as visited
Enqueue(Start)
While queue is not empty
    Vertex = Dequeue()
    Print Vertex
    For each Neighbor of Vertex
        If Neighbor is not visited
            Mark Neighbor as visited
            Enqueue(Neighbor)
        End If
    End For
End While

## DFS ##
DFS(Graph, Start)
Mark Start as visited
Print Start
For each Neighbor of Start
    If Neighbor is not visited
        DFS(Graph, Neighbor)
    End If
End For
