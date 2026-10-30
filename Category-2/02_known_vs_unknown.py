class DeliveryEnvironment:
    def __init__(self):
        self.actual_costs = {"A-B": 2, "B-C": 4, "A-C": 7}
        self.learned_costs = {}

    def known_environment(self):
        print("Available Road Information:")
        for road, cost in self.actual_costs.items():
            print(road, "=", cost)

    def explore_road(self, road):
        if road in self.actual_costs:
            cost = self.actual_costs[road]
            self.learned_costs[road] = cost
            print("Explored Road:", road, "| Learned Cost:", cost)
        else:
            print("Road Not Available")

    def display_knowledge(self):
        print("Learned Information:", self.learned_costs)


def main():
    environment = DeliveryEnvironment()
    print("KNOWN ENVIRONMENT")
    environment.known_environment()

    print("\nUNKNOWN ENVIRONMENT")
    environment.display_knowledge()

    print("\nRobot Starts Exploring")
    for road in ["A-B", "B-C", "A-C"]:
        environment.explore_road(road)

    print("\nAfter Learning:")
    environment.display_knowledge()
    print("Known: Agent already knows the environment rules.")
    print("Unknown: Agent learns the rules through experience.")


if __name__ == "__main__":
    main()
