
PI = 3.14159

def area_of_circle(r):
    return PI * r ** 2

def is_even(n):
    return n % 2 == 0

if __name__ == "__main__":
    # runs only with:  python mymath_utils.py   (not when imported)
    print("Running as a script:", area_of_circle(2))
