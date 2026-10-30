# Min-conflicts local search for the N-Queens constraint satisfaction problem.
import random
def conflicts(board,row,col):
    return sum(1 for c,r in enumerate(board) if c!=col and
               (r==row or abs(r-row)==abs(c-col)))
def solve(n=8,max_steps=10000):
    board=[random.randrange(n) for _ in range(n)]
    for step in range(max_steps):
        bad=[c for c in range(n) if conflicts(board,board[c],c)>0]
        if not bad: return board,step
        col=random.choice(bad)
        values=[conflicts(board,r,col) for r in range(n)]
        best=min(values); board[col]=random.choice([r for r,v in enumerate(values) if v==best])
    return None,max_steps
solution,steps=solve()
if solution:
    print("Solution in",steps,"steps:")
    for row in range(8): print(" ".join("Q" if solution[c]==row else "." for c in range(8)))
else: print("No solution this run; execute again.")
