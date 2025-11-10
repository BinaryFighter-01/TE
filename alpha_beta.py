# Alpha–Beta Pruning Algorithm

def alphabeta(depth, index, isMax, values, alpha, beta):
    # Terminal condition: depth == 3 means leaf node
    if depth == 3:
        return values[index]

    if isMax:
        best = float('-inf')
        for i in range(2):
            val = alphabeta(depth + 1, index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # Prune Branch
        return best

    else:
        best = float('inf')
        for i in range(2):
            val = alphabeta(depth + 1, index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break  # Prune Branch
        return best


# Leaf node values
values = [3, 5, 8, 9, 1, 6, 3, 0, -1, -2]

print("Alpha–Beta Result:", alphabeta(0, 0, True, values, float('-inf'), float('inf')))
