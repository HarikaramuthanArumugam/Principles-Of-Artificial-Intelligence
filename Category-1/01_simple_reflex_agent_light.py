def light_agent(motion, brightness):
    if motion == "yes" and brightness == "dark":
        return "Light ON"
    return "Light OFF"


def show_result(motion, brightness):
    print("Motion:", motion)
    print("Brightness:", brightness)
    print("Action:", light_agent(motion, brightness))
    print("-" * 35)


def main():
    print("SIMPLE REFLEX AGENT - LIGHT CONTROL")
    print("-----------------------------------")
    print("The agent uses current sensor readings.")

    test_cases = [
        ("yes", "dark"),
        ("yes", "bright"),
        ("no", "dark"),
        ("no", "bright")
    ]

    for number, (motion, brightness) in enumerate(test_cases, start=1):
        print("\nTest Case:", number)
        show_result(motion, brightness)

    print("Interactive Mode")
    motion = input("Is motion detected? (yes/no): ").lower()
    brightness = input("Is the room dark or bright? ").lower()

    if motion in ["yes", "no"] and brightness in ["dark", "bright"]:
        show_result(motion, brightness)
    else:
        print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
