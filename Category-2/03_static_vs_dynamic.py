class CleaningEnvironment:
    def __init__(self):
        self.rooms = {"A": "Dirty", "B": "Clean", "C": "Dirty"}

    def display_rooms(self):
        print("Room Conditions:")
        for room, status in self.rooms.items():
            print(room, ":", status)

    def clean_room(self, room):
        if room in self.rooms:
            self.rooms[room] = "Clean"
            print("Robot cleaned room:", room)

    def add_dirt(self, room):
        self.rooms[room] = "Dirty"
        print("New dirt appeared in room:", room)


def main():
    print("STATIC ENVIRONMENT")
    static_room = CleaningEnvironment()
    static_room.display_rooms()
    static_room.clean_room("A")
    static_room.display_rooms()
    print("The environment remains unchanged by itself.")

    print("\nDYNAMIC ENVIRONMENT")
    dynamic_room = CleaningEnvironment()
    dynamic_room.display_rooms()
    dynamic_room.clean_room("A")
    dynamic_room.add_dirt("B")
    dynamic_room.display_rooms()
    dynamic_room.clean_room("B")
    dynamic_room.display_rooms()

    print("Static: Environment does not change independently.")
    print("Dynamic: Environment can change while the agent works.")


if __name__ == "__main__":
    main()
