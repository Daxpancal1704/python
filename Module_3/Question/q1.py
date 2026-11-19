"""### Question 1 (Easy) - A class for a driver
Create a class `Driver` with the attributes `name`, `team` and `points` (starts at `0`). Add a method `add_points(n)` and a `__str__` that returns text in the format shown.

```python
d1 = Driver("Lando Norris", "McLaren")
d1.add_points(25)
d1.add_points(18)
print(d1)

d2 = Driver("Kimi Antonelli", "Mercedes")
print(d2)
```
```
Lando Norris (McLaren) - 43 points
Kimi Antonelli (Mercedes) - 0 points
```"""



class Driver:
    def __init__(self,name,team):
        self.name=name
        self.team=team
        self.point=0

    def add_points(self,n):
        self.point += n

    def __str__(self):
        return f"Driver: {self.name} ({self.team}) - {self.point} Points"


d1=Driver("Lando Norris","Mclaren")
d1.add_points(23)    
d1.add_points(23)
print(d1)    
d2=Driver("Kimi Antonwlli","Mercedes")
d2.add_points(23)
d2.add_points(213)
print(d2)