"""Question 5
An F1 team wants a small tool that turns a driver's race results into championship points.
Write two files: one holds the functions, the other imports and uses them."""

"""
Only the top 10 finishers score. Every other position scores 0.
Position 1 2 3 4 5 6 7 8 9 10
Points 25 18 15 12 10 8 6 4 2 1
A driver who does not finish a race is recorded as DNF and scores 0 points."""

""""
File 1: q5_f1_tools.py - three functions. They only return values: no input() and
no print(), and nothing may run when the file is imported.
Function Returns
get_points(position) the points for one race result. position is an integer
or the text "DNF"
total_points(results) the total points for a list of results
podium_count(results) the number of podium finishes (positions 1, 2 or 3) in a
list of results"""


"""File 2: q5_main.py - imports the three functions from q5_f1_tools. Read the driver's
name, then one line of results separated by spaces (numbers and DNF). Print the summary.
Put the program inside an if __name__ == "__main__": block.
The best finish is the smallest position number, ignoring DNF. If every result is DNF, print
N/A. If no results are entered, print No races entered.
Sample input
Enter driver name: Lando
Enter results: 1 3 DNF 2 5
Sample output
Driver: Lando
Races: 5
Points: 68
Podiums: 3
Best finish: 1
For the results DNF DNF the output is Races: 2, Points: 0, Podiums: 0 and Best
finish: N/A."""
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
