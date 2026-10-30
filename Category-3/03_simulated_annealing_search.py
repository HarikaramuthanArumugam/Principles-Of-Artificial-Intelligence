import random
import math


def objective(x):
    return -(x - 7) ** 2 + 49


def simulated_annealing(start):
    current = start
    best = current
    temperature = 10.0
    cooling_rate = 0.85

    while temperature > 0.1:
        candidate = current + random.choice([-2, -1, 1, 2])
        candidate = max(0, min(10, candidate))
        difference = objective(candidate) - objective(current)

        if difference > 0:
            current = candidate
        else:
            probability = math.exp(difference / temperature)
            if random.random() < probability:
                current = candidate

        if objective(current) > objective(best):
            best = current

        print("Temperature:", round(temperature, 2),
              "| Current:", current,
              "| Value:", objective(current))
        temperature *= cooling_rate

    return best


def main():
    random.seed(4)
    print("SIMULATED ANNEALING SEARCH")
    try:
        start = int(input("Enter starting value (0-10): "))
    except ValueError:
        print("Please enter an integer.")
        return

    if not 0 <= start <= 10:
        print("Invalid starting value.")
        return

    best = simulated_annealing(start)
    print("\nBest State Found:", best)
    print("Best Objective Value:", objective(best))


if __name__ == "__main__":
    main()
