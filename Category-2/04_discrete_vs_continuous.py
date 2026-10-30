class DiscreteRobot:
    def __init__(self):
        self.position = 0

    def move(self, direction):
        if direction == "right":
            self.position += 1
        elif direction == "left":
            self.position -= 1
        print("Discrete Position:", self.position)


class ContinuousRobot:
    def __init__(self):
        self.position = 0.0

    def move(self, speed, time):
        self.position += speed * time
        print("Continuous Position:", round(self.position, 2))


def main():
    print("DISCRETE ENVIRONMENT")
    robot1 = DiscreteRobot()
    robot1.move("right")
    robot1.move("right")
    robot1.move("left")
    robot1.move("right")
    print("Position changes in separate steps.")

    print("\nCONTINUOUS ENVIRONMENT")
    robot2 = ContinuousRobot()
    robot2.move(1.5, 0.5)
    robot2.move(2.0, 1.2)
    robot2.move(0.8, 0.7)
    print("Position changes continuously.")

    print("Discrete: Values change in separate steps.")
    print("Continuous: Values can change smoothly.")


if __name__ == "__main__":
    main()
