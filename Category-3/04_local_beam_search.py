def calculate_score(location):
    return -(location - 8) ** 2 + 64


def get_neighbours(location):
    neighbours = []
    if location > 0:
        neighbours.append(location - 1)
    if location < 10:
        neighbours.append(location + 1)
    return neighbours


def local_beam_search(initial_states, beam_width):
    beam = initial_states[:]
    print("Initial States:", beam)

    for step in range(1, 6):
        candidates = []
        for state in beam:
            candidates.extend(get_neighbours(state))

        candidates = list(set(candidates))
        candidates.sort(key=calculate_score, reverse=True)
        beam = candidates[:beam_width]

        print("\nStep:", step)
        print("Selected States:", beam)
        for state in beam:
            print("Location:", state, "| Score:", calculate_score(state))

        if not beam:
            return None

    return max(beam, key=calculate_score)


def main():
    print("LOCAL BEAM SEARCH")
    initial_states = [1, 4, 9]
    beam_width = 2

    print("Finding the best solar plant location.")
    print("Initial States:", initial_states)
    print("Beam Width:", beam_width)

    result = local_beam_search(initial_states, beam_width)
    print("\nSEARCH COMPLETED")
    print("Best Location:", result)
    if result is not None:
        print("Maximum Score:", calculate_score(result))
    print("Local Beam Search maintains multiple candidate states.")


if __name__ == "__main__":
    main()
