def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbour in reversed(graph.get(node, [])):
                if neighbour not in visited:
                    stack.append(path + [neighbour])

    return None


def main():
    print("DEPTH FIRST SEARCH")
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": ["H"],
        "E": [],
        "F": [],
        "G": ["I"],
        "H": [],
        "I": []
    }

    start = input("Enter starting room (A-I): ").upper()
    goal = input("Enter target room (A-I): ").upper()

    if start not in graph or goal not in graph:
        print("Invalid room.")
        return

    result = dfs(graph, start, goal)
    if result:
        print("Path Found:", " -> ".join(result))
        print("Number of Steps:", len(result) - 1)
    else:
        print("Target room not found.")

    print("DFS explores one branch deeply before backtracking.")


if __name__ == "__main__":
    main()
