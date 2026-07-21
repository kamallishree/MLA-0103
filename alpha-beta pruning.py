MAX = 1000
MIN = -1000
def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta, maxDepth):
    if depth == maxDepth:
        return values[nodeIndex]
    if maximizingPlayer:
        best = MIN
        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta, maxDepth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta, maxDepth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
depth = int(input("Enter depth of the game tree: "))
n = 2 ** depth
print("Enter", n, "leaf node values:")
values = list(map(int, input().split()))
result = alphabeta(0, 0, True, values, MIN, MAX, depth)
print("The optimal value is:", result)
