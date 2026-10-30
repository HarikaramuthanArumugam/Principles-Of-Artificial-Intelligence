class GPSAgent:
    def __init__(self, roads):
        self.roads = roads
        self.current_location = "Home"
        self.goal = "College"

    def find_route(self, start, goal):
        queue = [[start]]
        visited = []

        while queue:
            path = queue.pop(0)
            place = path[-1]

            if place == goal:
                return path

            if place not in visited:
                visited.append(place)
                for neighbour in self.roads.get(place, []):
                    if neighbour not in visited:
                        queue.append(path + [neighbour])

        return None

    def display_route(self, route):
        if route:
            print("Goal Reached:", self.goal)
            print("Route:", " -> ".join(route))
            print("Steps:", len(route) - 1)
        else:
            print("No route is available.")

    def navigate(self, start, goal):
        self.current_location = start
        self.goal = goal
        print("\nStarting Point:", start)
        print("Destination:", goal)
        route = self.find_route(start, goal)
        self.display_route(route)


def main():
    print("GOAL-BASED AGENT - GPS NAVIGATION")
    roads = {
        "Home": ["Park", "Market"],
        "Park": ["Library"],
        "Market": ["Hospital"],
        "Library": ["College"],
        "Hospital": ["College"],
        "College": []
    }

    agent = GPSAgent(roads)
    agent.navigate("Home", "College")
    agent.navigate("Home", "Hospital")

    print("\nCustom Navigation")
    start = input("Starting place (Home/Park/Market): ").title()
    goal = input("Destination (College/Library/Hospital): ").title()

    if start in roads and goal in roads:
        agent.navigate(start, goal)
    else:
        print("Invalid location.")


if __name__ == "__main__":
    main()
