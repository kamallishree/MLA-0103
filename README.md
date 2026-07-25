## BFS  ##
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


## ALPHA BETA PRUNING ##
START

Input the depth of the game tree

Calculate the number of leaf nodes (2^depth)

Input the leaf node values

Initialize Alpha = -∞

Initialize Beta = +∞

Call AlphaBeta(Root, Depth, Alpha, Beta, TRUE)

Print the optimal value

STOP

Procedure AlphaBeta(Node, Depth, Alpha, Beta, MaximizingPlayer)

    If Depth = 0
        Return the value of the current node
    End If

    If MaximizingPlayer is TRUE

        Best = -∞

        For each child of the current node

            Best = max(Best, AlphaBeta(Child, Depth - 1, Alpha, Beta, FALSE))

            Alpha = max(Alpha, Best)

            If Alpha ≥ Beta
                Break
            End If

        End For

        Return Best

    Else

        Best = +∞

        For each child of the current node

            Best = min(Best, AlphaBeta(Child, Depth - 1, Alpha, Beta, TRUE))

            Beta = min(Beta, Best)

            If Alpha ≥ Beta
                Break
            End If

        End For

        Return Best

    End If

End Procedure

## MARCUS ##

START

Declare Marcus as a man.
Declare Marcus as a Pompeian.
Declare Caesar as a ruler.
Declare that Marcus tried to assassinate Caesar.

IF a person is a Pompeian
    THEN declare the person as a Roman.

IF a person is a man
    THEN declare the person as a person.

IF a person tried to assassinate a ruler
    THEN declare the person is not loyal to that ruler.

IF a Roman is not loyal to Caesar
    THEN declare that Roman hates Caesar.

IF a Roman is loyal to Caesar
    THEN declare the Roman is loyal to Caesar.

Check whether Marcus is loyal to Caesar.
Display the result.

Check whether Marcus hates Caesar.
Display the result.

STOP
