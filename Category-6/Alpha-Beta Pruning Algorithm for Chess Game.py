# Alpha-Beta pruning on a small chess-inspired game tree.
tree={"Root":["Move A","Move B"],"Move A":["Reply A1","Reply A2"],"Move B":["Reply B1","Reply B2"],"Reply A1":[],"Reply A2":[],"Reply B1":[],"Reply B2":[]}
scores={"Reply A1":4,"Reply A2":6,"Reply B1":2,"Reply B2":8}
visited=[]
def alpha_beta(node,alpha,beta,maximizing):
    if not tree[node]: visited.append(node); return scores[node]
    if maximizing:
        value=float("-inf")
        for child in tree[node]:
            value=max(value,alpha_beta(child,alpha,beta,False)); alpha=max(alpha,value)
            if alpha>=beta: print("Pruned branch below",node); break
        return value
    value=float("inf")
    for child in tree[node]:
        value=min(value,alpha_beta(child,alpha,beta,True)); beta=min(beta,value)
        if beta<=alpha: print("Pruned branch below",node); break
    return value
print("Best score:",alpha_beta("Root",float("-inf"),float("inf"),True))
print("Evaluated leaf positions:",visited)
print("Chess-inspired search demonstration, not a complete chess engine.")
