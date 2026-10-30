from collections import deque


def build_path(parent, node):
    path = []
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]


def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    front_queue = deque([start])
    back_queue = deque([goal])
    front_parent = {start: None}
    back_parent = {goal: None}

    while front_queue and back_queue:
        current = front_queue.popleft()
        for neighbour in graph.get(current, []):
            if neighbour not in front_parent:
                front_parent[neighbour] = current
                front_queue.append(neighbour)
            if neighbour in back_parent:
                first = build_path(front_parent, neighbour)
                second = build_path(back_parent, neighbour)
                return first + second[-2::-1]

        current = back_queue.popleft()
        for neighbour in graph.get(current, []):
            if neighbour not in back_parent:
                back_parent[neighbour] = current
                back_queue.append(neighbour)
            if neighbour in front_parent:
                first = build_path(front_parent, neighbour)
                second = build_path(back_parent, neighbour)
                return first + second[-2::-1]

    return None


def main():
    print("BIDIRECTIONAL SEARCH")
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "E"],
        "D": ["B", "F"],
        "E": ["C", "F"],
        "F": ["D", "E"]
    }

    start = input("Enter starting node (A-F): ").upper()
    goal = input("Enter destination node (A-F): ").upper()

    if start not in graph or goal not in graph:
        print("Invalid node.")
        return

    result = bidirectional_search(graph, start, goal)
    if result:
        print("Path Found:", " -> ".join(result))
        print("Number of Steps:", len(result) - 1)
    else:
        print("No path found.")

    print("Bidirectional Search starts from both directions.")
    print("It stops when the two searches meet.")


if __name__ == "__main__":
    main()
