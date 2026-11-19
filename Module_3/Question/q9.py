"""### Question 9 (Hard) - Fastest lap
A list of lap records is given. Valid lines look exactly like `Lap <number> | <driver> | <m>:<ss.mmm>`; other lines are invalid.
```python
log = ["Lap 1 | Norris | 1:25.300",
       "Lap 2 | Piastri | 1:24.800",
       "Lap 3 | Norris | 1:24.250",
       "Lap 4 | pit stop",
       "Lap 5 | Piastri | 1:24.900"]
```
1. Use `re.fullmatch()` with **groups** to read each valid line (lap number, driver, time).
2. Convert each time to **seconds** (`1:24.250` -> `84.25`).
3. Use `reduce()` with a `lambda` to find the fastest lap.
4. Count the invalid lines.

```
Valid laps: 4
Invalid lines: 1
Fastest lap: Norris - 84.25 s (lap 3)
```"""

#import re moduel because find the pattern using re.fullmatch 
import re
#use reduce because search the fastest lap  and pick the one winner
from functools import reduce



log = ["Lap 1 | Norris | 1:25.300",
       "Lap 2 | Piastri | 1:24.800",
       "Lap 3 | Norris | 1:24.250",
       "Lap 4 | pit stop",
       "Lap 5 | Piastri | 1:24.900"]

# it's pattern to find log
    #     Lap (use for number)
    #                   use for drive name 
    #                                  (minit) (sec) (minut)
pattern=r"Lap (\d+) \| ([a-zA-Z]+) \| (\d+):(\d{2}\.\d{3})"

valid_lap=[]
invalid_line=0

for line in log:
    match=re.fullmatch(pattern,line)

    if match:
        lap_num=int(match.group(1))
        driver=match.group(2)
        minute=int(match.group(3))
        second=float(match.group(4))

        total_seond=minute * 60 + second
        valid_lap.append((lap_num,driver,total_seond))
    else:
        invalid_line +=1

fastest=reduce(lambda a, b : a if a[2] < b[2] else b,valid_lap)

print(f"valid laps : {len(valid_lap)}")
print(f"invalid line : {invalid_line}")
print(f"fastest lap :{fastest[1]}-{fastest[2]:.2f} s (lap{fastest[0]})")