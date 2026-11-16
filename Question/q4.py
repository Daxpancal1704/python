"""### Question 4 (Medium) - Functional programming
Read one line of space-separated integers. Using `lambda` with `map()`, `filter()` and `reduce()` (no loops and no comprehensions), print:
1. the **cube** of every number (as a list)
2. only the numbers **divisible by 3** (as a list)
3. the **product** of all the numbers

```
2 3 4 6
```
```
[8, 27, 64, 216]
[3, 6]
144
```"""
from functools import reduce

Numbers=list(map(int, input("Enter number : ").split()))


cube=list(map(lambda x : x ** 3, Numbers))
print(cube)

divisble=list(filter(lambda x : x % 3==0 , Numbers))
print(divisble)

product=reduce(lambda x,y :x * y ,Numbers )
print(product)