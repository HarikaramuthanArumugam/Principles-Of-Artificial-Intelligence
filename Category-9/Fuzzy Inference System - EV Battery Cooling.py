# Fuzzy Inference System - EV Battery Cooling

def membership(value, low, middle, high):

    if value <= low:
        return 0

    elif value <= middle:
        return (value - low) / (middle - low)

    elif value <= high:
        return (high - value) / (high - middle)

    else:
        return 0


def fuzzy_inference(temperature, load):

    # Temperature membership values
    low_temp = membership(temperature, 0, 30, 60)
    medium_temp = membership(temperature, 30, 60, 90)
    high_temp = membership(temperature, 60, 90, 120)

    # Motor load membership values
    low_load = membership(load, 0, 30, 60)
    medium_load = membership(load, 30, 60, 90)
    high_load = membership(load, 60, 90, 120)

    # Fuzzy IF-THEN rules
    rules = [
        (min(low_temp, low_load), 10),
        (min(low_temp, medium_load), 30),
        (min(low_temp, high_load), 50),
        (min(medium_temp, low_load), 40),
        (min(medium_temp, medium_load), 60),
        (min(medium_temp, high_load), 80),
        (min(high_temp, low_load), 70),
        (min(high_temp, medium_load), 90),
        (min(high_temp, high_load), 100)
    ]

    # Defuzzification
    numerator = sum(a * b for a, b in rules)
    denominator = sum(a for a, b in rules)

    if denominator == 0:
        return 0

    return numerator / denominator


def main():

    print("FUZZY INFERENCE - EV BATTERY COOLING")
    print("------------------------------------")

    # Test cases: temperature and motor load
    test_cases = [
        (25, 20),
        (45, 35),
        (55, 45),
        (65, 55),
        (75, 60),
        (85, 90),
        (95, 80),
        (40, 70),
        (100, 100),
        (30, 50)
    ]

    for i, (temperature, load) in enumerate(test_cases, 1):

        cooling = fuzzy_inference(temperature, load)

        print("\nTest Case:", i)
        print("Battery Temperature:", temperature)
        print("Motor Load:", load)
        print("Cooling Level:", round(cooling, 2), "%")

        if cooling < 40:
            print("Cooling Status: LOW")
        elif cooling < 70:
            print("Cooling Status: MEDIUM")
        else:
            print("Cooling Status: HIGH")


if __name__ == "__main__":
    main()
