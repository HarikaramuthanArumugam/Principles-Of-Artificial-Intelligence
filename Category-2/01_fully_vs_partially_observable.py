class RoomEnvironment:
    def __init__(self):
        self.rooms = {"A": "Clear", "B": "Obstacle", "C": "Clear"}
        self.position = "A"

    def fully_observable(self):
        return self.rooms.copy()

    def partially_observable(self):
        return {self.position: self.rooms[self.position]}

    def move(self, room):
        if room in self.rooms:
            self.position = room
            print("Robot moved to:", room)
        else:
            print("Invalid room")


def main():
    environment = RoomEnvironment()
    print("FULLY OBSERVABLE ENVIRONMENT")
    for room, status in environment.fully_observable().items():
        print(room, ":", status)

    print("\nPARTIALLY OBSERVABLE ENVIRONMENT")
    print("Available Information:", environment.partially_observable())
    environment.move("B")
    print("New Observation:", environment.partially_observable())

    print("\nFully Observable: Complete information is available.")
    print("Partially Observable: Only limited information is available.")


if __name__ == "__main__":
    main()
