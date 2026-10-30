def depth_limited_search(graph, node, goal, limit, path=None):
    if path is None:
        path = []

    path = path + [node]
    if node == goal:
        return path

    if limit == 0:
        return None

    for neighbour in graph.get(node, []):
        if neighbour not in path:
            result = depth_limited_search(
                graph, neighbour, goal, limit - 1, path
            )
            if result:
                return result

    return None


def main():
    print("DEPTH LIMITED SEARCH")
    graph = {
        "Home": ["News", "Sports"],
        "News": ["Local", "World"],
        "Sports": ["Cricket", "Football"],
        "Local": ["Article1"],
        "World": ["Article2"],
        "Cricket": [],
        "Football": [],
        "Article1": [],
        "Article2": []
    }

    start = input("Enter starting page: ").title()
    goal = input("Enter target page: ").title()

    try:
        limit = int(input("Enter depth limit: "))
    except ValueError:
        print("Depth limit must be an integer.")
        return

    if start not in graph or goal not in graph or limit < 0:
        print("Invalid input.")
        return

    result = depth_limited_search(graph, start, goal, limit)
    if result:
        print("Page Found:", " -> ".join(result))
        print("Depth:", len(result) - 1)
    else:
        print("Target not found within the depth limit.")

    print("DLS explores nodes only up to a fixed depth.")


if __name__ == "__main__":
    main()
