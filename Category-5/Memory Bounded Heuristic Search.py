# Memory-bounded heuristic best-first search for a small route map.
# This teaching version caps the frontier; it is not a full SMA* implementation.
graph={"Home":{"Park":2,"Mall":5,"School":4},"Park":{"Home":2,"Museum":4,"Lake":6},"Mall":{"Home":5,"Museum":2},"School":{"Home":4,"Lake":3},"Museum":{"Park":4,"Mall":2,"Goal":5},"Lake":{"Park":6,"School":3,"Goal":2},"Goal":{"Museum":5,"Lake":2}}
h={"Home":7,"Park":5,"Mall":4,"School":4,"Museum":2,"Lake":1,"Goal":0}
def memory_bounded(start,goal,limit=3):
    frontier=[(h[start],0,start,[start])]; best={start:0}
    while frontier:
        frontier.sort(key=lambda x:x[0]); f,g,u,path=frontier.pop(0)
        print("Expanding",u,"f =",f)
        if u==goal: return path,g
        for v,c in graph[u].items():
            ng=g+c
            if ng<best.get(v,float("inf")):
                best[v]=ng; frontier.append((ng+h[v],ng,v,path+[v]))
        frontier.sort(key=lambda x:x[0])
        while len(frontier)>limit:
            removed=frontier.pop(); print("Memory cap: discarded",removed[2])
    return None,float("inf")
p,c=memory_bounded("Home","Goal",3)
print("Path:", " -> ".join(p) if p else "Not found within memory limit","| Cost:",c)
