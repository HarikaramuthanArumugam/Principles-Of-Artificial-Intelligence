# Bayesian Reasoning - Medical Diagnosis

def bayesian_reasoning(prior, sensitivity, false_positive):

    # Calculate probability of positive test
    positive = prior * sensitivity

    # Calculate probability of false positive
    negative = (1 - prior) * false_positive

    # Apply Bayes' theorem
    result = positive / (positive + negative)

    return result * 100


def main():

    print("BAYESIAN REASONING - MEDICAL DIAGNOSIS")
    print("--------------------------------------")

    # Test cases: prior, sensitivity, false positive
    test_cases = [
        (0.10, 0.90, 0.05),
        (0.20, 0.95, 0.10),
        (0.01, 0.99, 0.02),
        (0.30, 0.85, 0.05),
        (0.15, 0.92, 0.04),
        (0.25, 0.88, 0.08),
        (0.05, 0.96, 0.03),
        (0.40, 0.90, 0.06),
        (0.12, 0.98, 0.02),
        (0.35, 0.93, 0.07)
    ]

    for i, test in enumerate(test_cases, 1):

        prior, sensitivity, false_positive = test

        result = bayesian_reasoning(
            prior, sensitivity, false_positive
        )

        print("\nTest Case:", i)
        print("Disease Probability:", prior * 100, "%")
        print("Test Sensitivity:", sensitivity * 100, "%")
        print("False Positive Rate:", false_positive * 100, "%")

        print("Final Disease Probability:",
              round(result, 2), "%")

        if result >= 50:
            print("Diagnosis: High Risk")
        else:
            print("Diagnosis: Low Risk")


if __name__ == "__main__":
    main()
