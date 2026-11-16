"""### Question 7 (Medium-Hard) - Abstraction and polymorphism
* Create an abstract class `Shape(ABC)` with an `__init__(label)`, an **abstract** method `area()` and a normal method `describe()` that returns `"<label> with area <area>"` (area with 2 decimals).
* Create `Circle(radius)` (use `math.pi`) and `Rectangle(width, height)`. Both call `super().__init__()` with their label.
* Loop over a list of different shapes and call `describe()` on each one.
* Show that `Shape("x")` cannot be created: catch the `TypeError` and print `Cannot create an object of an abstract class`.

```python
shapes = [Circle(5), Rectangle(4, 6)]
```
```
Circle with area 78.54
Rectangle with area 24.00
Cannot create an object of an abstract class
```"""


from abc import ABC ,abstractmethod
import math 


class Shape(ABC):
    """class Shape is abstractmethod """

    def __init__(self,label):
        self.label=label

    @abstractmethod
    def area(self):
        pass

    def describe(self):
        return f"{self.label} with area {self.area():.2f}"
    
class Circle(Shape):
    def __init__(self,radius):
        super().__init__("Circle")
        self.radius=radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width,height):
        super().__init__("Rectangle")
        self.width=width
        self.height=height

    def area(self):
        return self.width * self.height

Shape=[Circle(5),Rectangle(10,10)]

for shape in Shape:
    print(shape.describe())

try:
    s=Shape("X")
except TypeError:
    print("Cannot an object of anabstact class")