class EmailClassifier:
    def classify(self, email):
        if "offer" in email.lower():
            return "Spam"
        return "Not Spam"


class RouteAgent:
    def __init__(self):
        self.location = "A"
        self.path = ["A"]

    def move(self, next_location):
        self.location = next_location
        self.path.append(next_location)
        print("Robot moved to:", self.location)

    def display_path(self):
        print("Complete Path:", " -> ".join(self.path))


def main():
    print("EPISODIC ENVIRONMENT")
    classifier = EmailClassifier()
    emails = [
        "Special offer today",
        "Meeting at 10 AM",
        "Free offer available"
    ]

    for email in emails:
        print("Email:", email)
        print("Result:", classifier.classify(email))

    print("Each email is classified independently.")

    print("\nSEQUENTIAL ENVIRONMENT")
    robot = RouteAgent()
    robot.move("B")
    robot.move("C")
    robot.move("D")
    robot.display_path()

    print("Episodic: Each task is independent.")
    print("Sequential: Current actions affect future decisions.")


if __name__ == "__main__":
    main()
