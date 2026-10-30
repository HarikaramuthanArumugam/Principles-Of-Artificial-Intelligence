class SelfDrivingCar:
    def __init__(self):
        self.actions = ["Brake", "Maintain Speed", "Accelerate"]

    def calculate_utility(self, action, traffic, road, distance):
        score = 0

        if action == "Brake":
            score += 8 if traffic == "heavy" else 3
            score += 7 if road == "wet" else 2
            score += 8 if distance == "near" else 1
        elif action == "Maintain Speed":
            score += 7 if traffic == "moderate" else 4
            score += 7 if road == "dry" else 5
            score += 6 if distance == "far" else 3
        else:
            score += 8 if traffic == "low" else 1
            score += 8 if road == "dry" else 0
            score += 8 if distance == "far" else 0

        return score

    def choose_action(self, traffic, road, distance):
        utilities = {}
        for action in self.actions:
            utilities[action] = self.calculate_utility(
                action, traffic, road, distance
            )

        print("Utility Scores:")
        for action, score in utilities.items():
            print(action, ":", score)

        return max(utilities, key=utilities.get)


def main():
    print("UTILITY-BASED AGENT - SELF-DRIVING CAR")
    car = SelfDrivingCar()
    test_cases = [
        ("heavy", "wet", "near"),
        ("moderate", "dry", "far"),
        ("low", "dry", "far")
    ]

    for number, (traffic, road, distance) in enumerate(test_cases, start=1):
        print("\nTest Case:", number)
        print("Traffic:", traffic)
        print("Road:", road)
        print("Obstacle Distance:", distance)
        print("Selected Action:",
              car.choose_action(traffic, road, distance))


if __name__ == "__main__":
    main()
