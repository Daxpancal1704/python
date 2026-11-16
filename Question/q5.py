"""### Question 5 (Medium) - Inheritance
Create three classes:
* `Vehicle(name, speed)` with a method `info()` that prints `Vehicle: <name>, top speed <speed> km/h`.
* `Car(Vehicle)` adds `doors`. Its `info()` first calls the parent's `info()` (use `super()`), then prints `Doors: <doors>`.
* `ElectricCar(Car)` adds `battery`. Its `info()` first calls the parent's `info()`, then prints `Battery: <battery> kWh`.

```python
e = ElectricCar("Tesla", 250, 4, 75)
e.info()
```
```
Vehicle: Tesla, top speed 250 km/h
Doors: 4
Battery: 75 kWh
```"""


#creat a Parent class 
class Vehical:
    """Create class with init() methods with name and speed parameter and creafe info(): method name and print vehical name and speed """
    
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed

    def info(self):
        print(f"Vehical : {self.name} , top spped : {self.speed} km/h.")

class Car(Vehical):

    """Inherit Vehcial class (parent) and calling the parameter with super() methods and add the another parameter that is call Doors."""

    def __init__(self, name, speed,Doors):
        #calling super() methods to access the parent calss parameter 
        super().__init__(name, speed)
        self.Doors=Doors
        
    # create infor method to print Doors.
    def info(self):
        super().info()
        print(f"Doors : {self.Doors}")


class ElectricCar(Car):
    """inherit chlid class (car) and calling the init method and paramter to user super() method.
    and add the another new parameter that is caled battery"""
    def __init__(self, name, speed, Doors,battery):
        super().__init__(name, speed, Doors)
        self.battery=battery

    def info(self):
        super().info()
        print(f"Battery : {self.battery} kWh")


e=ElectricCar("Tesla" ,250,4,70)
e.info()


        