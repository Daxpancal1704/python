"""### Question 10 (Hardest) - Season planner
Build a small planner that uses OOP, regex, `datetime`, `reduce()` and `os` together.

* Create a class `Race` with `name` and `date` (a `datetime.date`), a `__str__`, a method `days_until(today)`, and a **class method** `from_text(text)` that reads text such as `"Dutch GP on 06-09-2026"` (use `re.fullmatch()` with groups and `datetime.strptime`). If the text does not match, or the date is not a real date, `from_text` must raise `ValueError`.
* Convert every line of the list below into a `Race` with `try/except`, and count the lines that were skipped.
* With `filter()` keep only the races after `today = date(2026, 9, 1)`, and with `reduce()` pick the earliest one.
* Create a folder `season` with `os.makedirs(..., exist_ok=True)` and write the line `Next race: <name> (<n> days away)` into `season/next_race.txt` (build the path with `os.path.join`).

```python
lines = ["Dutch GP on 06-09-2026",
         "Italian GP on 13-09-2026",
         "Spanish GP on 32-09-2026",      # not a real date
         "Singapore GP - 2026"]           # wrong format
```
```
Valid races: 2
Skipped: 2
Next race: Dutch GP (5 days away)
Saved to season/next_race.txt
```"""


import os
import re
from functools import reduce
from datetime import datetime,date


class Race:
    def __init__(self,name,race_date):
        self.name=name
        self.race_date=race_date

    def __str__(self):
        return f"{self.name} ({self.date.strftime('%d-%m-%Y')})"

    def days_until(self,today):
        return (self.date-today).days

    @classmethod
    def from_text(cls,text):
        match=re.fullmatch(r"(.+?)\s+on\s+(\d{2}-\d{2}-\d{4})",text.strip())

        if not match:
            raise ValueError(f"Invalid formate : {text}")

        name,date_str=match.group()

        #straptime is autiomatically raise valueerror for impossible dates like 32-09-2026
        race_date=datetime.strptime(date_str,"%d-%m-%Y").date()
        return cls(name,race_date)

lines = [
    "Dutch GP on 06-09-2026",
    "Italian GP on 13-09-2026",
    "Spanish GP on 32-09-2026",      # not a real date
    "Singapore GP - 2026"            # wrong format
]

valid_race=[]
skippd=0

for line in lines:

    try:
        valid_race.append(Race.from_text(line))
    except ValueError:
        skippd +=1

print(f"valid races :{len(valid_race)}")
print(f"Skipped: {skippd}")