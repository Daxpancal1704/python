
from testq5 import get_points, total_points, podium_count


def main():
    name = input("Enter driver name: ")
    user_input = input("Enter results: ").split()

    results = []

    for result in user_input:
        if result == "DNF":
            results.append("DNF")
        else:
            results.append(int(result))

    if len(results) == 0:
        print("No races entered.")
        return

    finishes = [p for p in results if p != "DNF"]

    if finishes:
        best_finish = min(finishes)
    else:
        best_finish = "N/A"

    print("Driver:", name)
    print("Races:", len(results))
    print("Points:", total_points(results))
    print("Podiums:", podium_count(results))
    print("Best finish:", best_finish)


if __name__ == "__main__":
    main()
