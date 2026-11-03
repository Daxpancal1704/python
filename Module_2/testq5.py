
def get_points(position):
    points = {
        1: 25,
        2: 18,
        3: 15,
        4: 12,
        5: 10,
        6: 8,
        7: 6,
        8: 4,
        9: 2,
        10: 1
    }

    if position == "DNF":
        return 0

    return points.get(position, 0)


def total_points(results):
    total = 0

    for position in results:
        total += get_points(position)

    return total


def podium_count(results):
    count = 0

    for position in results:
        if position in (1, 2, 3):
            count += 1

    return count
