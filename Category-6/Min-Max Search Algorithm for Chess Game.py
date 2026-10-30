# Minimax on a small chess-inspired evaluation tree (not a full chess engine).
# Scores are from White's perspective: positive is good for White.
tree={"Root":["White Move A","White Move B"],"White Move A":["Black Reply A1","Black Reply A2"],"White Move B":["Black Reply B1","Black Reply B2"],"Black Reply A1":[],"Black Reply A2":[],"Black Reply B1":[],"Black Reply B2":[]}
scores={"Black Reply A1":3,"Black Reply A2":5,"Black Reply B1":2,"Black Reply B2":9}
def minimax(node,maximizing):
    if not tree[node]: return scores[node]
    values=[minimax(child,not maximizing) for child in tree[node]]
    return max(values) if maximizing else min(values)
for move in tree["Root"]: print(move,"score:",minimax(move,False))
best=max(tree["Root"],key=lambda move:minimax(move,False))
print("White should choose:",best)
print("This is a search-tree demonstration; legal chess moves and board evaluation are not implemented.")
