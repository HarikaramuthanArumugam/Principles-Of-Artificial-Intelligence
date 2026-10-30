def objective(x):
    return -(x - 6) ** 2 + 36


def hill_climbing(start):
    current = start
    print("Starting Position:", current)
    print("Starting Value:", objective(current))

    while True:
        neighbours = []
        if current - 1 >= 0:
            neighbours.append(current - 1)
        if current + 1 <= 10:
            neighbours.append(current + 1)

        if not neighbours:
            break

        best = max(neighbours, key=objective)
        if objective(best) <= objective(current):
            break

        current = best
        print("Moving to:", current)
        print("Current Value:", objective(current))

    return current


def main():
    print("HILL CLIMBING SEARCH")
    try:
        start = int(input("Enter starting position (0-10): "))
    except ValueError:
        print("Please enter an integer.")
        return

    if not 0 <= start <= 10:
        print("Invalid starting position.")
        return

    result = hill_climbing(start)
    print("\nSEARCH COMPLETED")
    print("Best Position Found:", result)
    print("Maximum Value:", objective(result))
    print("Hill Climbing moves to a better neighbour.")
    print("It stops when no better neighbour is available.")


if __name__ == "__main__":
    main()
