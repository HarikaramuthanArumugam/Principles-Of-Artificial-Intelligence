from heapq import heappush, heappop
# Greedy Best-First Search: route planning using heuristic distance.
graph={"Arad":["Sibiu","Timisoara","Zerind"],"Sibiu":["Arad","Oradea","Fagaras","Rimnicu Vilcea"],"Timisoara":["Arad","Lugoj"],"Zerind":["Arad","Oradea"],"Oradea":["Zerind","Sibiu"],"Lugoj":["Timisoara","Mehadia"],"Mehadia":["Lugoj","Drobeta"],"Drobeta":["Mehadia","Craiova"],"Craiova":["Drobeta","Rimnicu Vilcea","Pitesti"],"Rimnicu Vilcea":["Sibiu","Craiova","Pitesti"],"Fagaras":["Sibiu","Bucharest"],"Pitesti":["Rimnicu Vilcea","Craiova","Bucharest"],"Bucharest":["Fagaras","Pitesti"]}
h={"Arad":366,"Sibiu":253,"Timisoara":329,"Zerind":374,"Oradea":380,"Lugoj":244,"Mehadia":241,"Drobeta":242,"Craiova":160,"Rimnicu Vilcea":193,"Fagaras":176,"Pitesti":100,"Bucharest":0}
def greedy(start,goal):
    q=[(h[start],start)]; parent={start:None}; seen=set()
    while q:
        _,u=heappop(q)
        if u in seen: continue
        seen.add(u); print("Visiting:",u)
        if u==goal:
            path=[]
            while u is not None: path.append(u); u=parent[u]
            return path[::-1]
        for v in graph[u]:
            if v not in seen and v not in parent: parent[v]=u; heappush(q,(h[v],v))
    return None
p=greedy("Arad","Bucharest")
print("Path:", " -> ".join(p) if p else "Not found")
