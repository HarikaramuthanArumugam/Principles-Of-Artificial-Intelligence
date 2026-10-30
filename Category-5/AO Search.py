# AO* Search Algorithm using an AND-OR graph

# Each list represents an alternative.
# Children within the same list must all be completed (AND).
# Different lists represent alternatives (OR).

graph = {
    "Start": [["PlanA"], ["PlanB", "PlanC"]],
    "PlanA": [["Task1"], ["Task2", "Task3"]],
    "PlanB": [["Task4"]],
    "PlanC": [["Task5"]],
    "Task1": [],
    "Task2": [],
    "Task3": [],
    "Task4": [],
    "Task5": []
}

# Cost of moving from one node to another
cost = {
    ("Start", "PlanA"): 1,
    ("Start", "PlanB"): 1,
    ("Start", "PlanC"): 1,
    ("PlanA", "Task1"): 2,
    ("PlanA", "Task2"): 1,
    ("PlanA", "Task3"): 1,
    ("PlanB", "Task4"): 3,
    ("PlanC", "Task5"): 2
}


def ao_star(node, visited=None):

    if visited is None:
        visited = set()

    if node in visited:
        raise ValueError("Cycle detected!")

    # Goal node
    if not graph[node]:
        return 0, [node]

    visited = visited | {node}

    minimum_cost = float("inf")
    best_solution = []

    # Explore alternative choices (OR)
    for option in graph[node]:

        total_cost = 0
        solution = [node]

        # Complete all children in this option (AND)
        for child in option:

            child_cost, child_solution = ao_star(
                child, visited
            )

            total_cost += cost[(node, child)] + child_cost
            solution.extend(child_solution)

        # Select the minimum-cost alternative
        if total_cost < minimum_cost:
            minimum_cost = total_cost
            best_solution = solution

    return minimum_cost, best_solution


# Main program
total_cost, solution = ao_star("Start")

print("AO* Search Solution:")
print(" -> ".join(solution))

print("Total Cost:", total_cost)
