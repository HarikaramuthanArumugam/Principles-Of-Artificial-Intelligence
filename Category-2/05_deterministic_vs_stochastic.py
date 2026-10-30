import random


class RobotEnvironment:
    def deterministic_move(self, position, action):
        if action == "right":
            return position + 1
        elif action == "left":
            return position - 1
        return position

    def stochastic_move(self, position, action):
        result = random.choice(["Success", "Slip"])
        if result == "Success":
            if action == "right":
                position += 1
            else:
                position -= 1
        print("Movement Result:", result)
        return position


def main():
    random.seed(5)
    environment = RobotEnvironment()

    print("DETERMINISTIC ENVIRONMENT")
    position = 0
    for action in ["right", "right", "left"]:
        position = environment.deterministic_move(position, action)
        print("Action:", action, "| New Position:", position)

    print("\nSTOCHASTIC ENVIRONMENT")
    position = 0
    for action in ["right", "right", "left", "right"]:
        position = environment.stochastic_move(position, action)
        print("Action:", action, "| New Position:", position)

    print("Deterministic: Results are predictable.")
    print("Stochastic: Results involve uncertainty.")


if __name__ == "__main__":
    main()
