import heapq

# Graph representing locations and travel costs
graph = {
    "A": {"B": 2, "C": 4},
    "B": {"A": 2, "D": 7, "E": 3},
    "C": {"A": 4, "E": 1},
    "D": {"B": 7, "G": 2},
    "E": {"B": 3, "C": 1, "G": 5},
    "G": {"D": 2, "E": 5}
}

# Heuristic values (estimated distance to goal G)
heuristic = {
    "A": 7,
    "B": 6,
    "C": 5,
    "D": 2,
    "E": 3,
    "G": 0
}

def a_star(start, goal):
    # Priority queue stores (f, g, current_node)
    priority_queue = [(heuristic[start], 0, start)]

    parent = {start: None}
    cost_so_far = {start: 0}

    while priority_queue:
        f, g, current = heapq.heappop(priority_queue)

        if g != cost_so_far[current]:
            continue

        print("Visiting:", current)

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path, g

        for neighbor, cost in graph[current].items():
            new_cost = g + cost

            if new_cost < cost_so_far.get(neighbor, float("inf")):
                cost_so_far[neighbor] = new_cost
                parent[neighbor] = current

                # f(n) = g(n) + h(n)
                f_value = new_cost + heuristic[neighbor]

                heapq.heappush(
                    priority_queue,
                    (f_value, new_cost, neighbor)
                )

    return None, float("inf")


# Main program
start = "A"
goal = "G"

path, total_cost = a_star(start, goal)

if path:
    print("\nA* Search Path:")
    print(" -> ".join(path))
    print("Total Cost:", total_cost)
else:
    print("Path not found!")
