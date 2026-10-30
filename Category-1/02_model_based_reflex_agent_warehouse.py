class WarehouseRobot:
    def __init__(self):
        self.position = "A"
        self.shelf_status = {
            "A": "unknown",
            "B": "unknown",
            "C": "unknown"
        }
        self.battery = 100

    def update_model(self, location, status):
        self.shelf_status[location] = status

    def choose_action(self):
        if self.battery <= 20:
            return "Return to charging station"

        for location in ["A", "B", "C"]:
            if self.shelf_status[location] == "unknown":
                return "Move to shelf " + location
            if self.shelf_status[location] == "item_found":
                return "Pick item from shelf " + location

        return "Return to starting point"

    def display_model(self):
        print("Position:", self.position)
        print("Shelf Memory:", self.shelf_status)
        print("Battery:", self.battery, "%")

    def perform_action(self, action):
        print("Action:", action)
        if action.startswith("Move to shelf"):
            self.position = action[-1]
            self.battery -= 10
        elif action.startswith("Pick item"):
            self.shelf_status[self.position] = "collected"
            self.battery -= 5
        elif action == "Return to starting point":
            self.position = "A"
            self.battery -= 10
        elif action == "Return to charging station":
            self.battery = 100


def main():
    print("MODEL-BASED REFLEX AGENT - WAREHOUSE ROBOT")
    robot = WarehouseRobot()
    observations = [
        ("A", "empty"),
        ("B", "item_found"),
        ("C", "empty")
    ]

    for location, status in observations:
        print("\nObservation:", location, "->", status)
        robot.update_model(location, status)
        robot.display_model()
        action = robot.choose_action()
        robot.perform_action(action)

    print("\nFinal Internal Model:")
    robot.display_model()
    print("Next Decision:", robot.choose_action())


if __name__ == "__main__":
    main()
