from collections import deque


def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    queue.append(path + [neighbour])

    return None


def main():
    print("BREADTH FIRST SEARCH")
    graph = {
        "Chennai": ["Vellore", "Bangalore"],
        "Vellore": ["Chennai", "Salem"],
        "Bangalore": ["Chennai", "Mysore"],
        "Salem": ["Vellore", "Coimbatore"],
        "Mysore": ["Bangalore", "Coimbatore"],
        "Coimbatore": ["Salem", "Mysore"]
    }

    start = input("Enter starting city: ").title()
    goal = input("Enter destination city: ").title()

    if start not in graph or goal not in graph:
        print("Invalid city name.")
        return

    result = bfs(graph, start, goal)
    if result:
        print("Path Found:", " -> ".join(result))
        print("Number of Steps:", len(result) - 1)
    else:
        print("No path found.")

    print("BFS explores nodes level by level.")
    print("It finds a shortest path in an unweighted graph.")


if __name__ == "__main__":
    main()
