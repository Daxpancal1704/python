def analyze_attendance(workshops):
    count = {}

    # Count workshop attendance for each student
    for workshop in workshops:
        for student in workshop:
            count[student] = count.get(student, 0) + 1

    # Unique attendees
    unique = len(count)

    # Common attendees
    common = []
    for student in count:
        if count[student] == len(workshops):
            common.append(student)

    # Exclusive attendees
    exclusive = []
    for student in count:
        if count[student] == 1:
            exclusive.append(student)

    # Repeat attendees
    repeat = []
    for student in count:
        if count[student] >= 2:
            repeat.append(student)

    # Exactly-two attendees
    exactly_two = []
    for student in count:
        if count[student] == 2:
            exactly_two.append(student)

    # Maximum overlap
    max_overlap = -1
    best_pair = None

    for i in range(len(workshops)):
        for j in range(i + 1, len(workshops)):
            overlap = len(set(workshops[i]) & set(workshops[j]))

            if overlap > max_overlap:
                max_overlap = overlap
                best_pair = (i + 1, j + 1)

    if best_pair is None:
        max_overlap = 0

    return {
        "Unique attendees": unique,
        "Common attendees": common,
        "Exclusive attendees": exclusive,
        "Repeat attendees": repeat,
        "Exactly-two attendees": exactly_two,
        "Maximum overlap": (best_pair, max_overlap)
    }


workshops = [
    [101, 102, 103, 104],
    [102, 103, 105],
    [102, 103, 106]
]

result = analyze_attendance(workshops)

for key, value in result.items():
    print(key, ":", value)