# Map-coloring CSP solved by backtracking with Minimum Remaining Values.
regions=["A","B","C","D","E"]
neighbors={"A":["B","C"],"B":["A","C","D"],"C":["A","B","D","E"],"D":["B","C","E"],"E":["C","D"]}
colors=["Red","Green","Blue"]; assignment={}
def valid(region,color):
    return all(assignment.get(n)!=color for n in neighbors[region])
def backtrack():
    if len(assignment)==len(regions): return True
    unassigned=[r for r in regions if r not in assignment]
    region=min(unassigned,key=lambda r:sum(valid(r,c) for c in colors))
    for color in colors:
        if valid(region,color):
            assignment[region]=color
            if backtrack(): return True
            del assignment[region]
    return False
if backtrack():
    print("Map-coloring solution:")
    for r in regions: print(r,":",assignment[r])
else: print("No solution.")
