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
    """Create class race: with name(it s string) and date(datetime.date) parameter"""
    def __init__(self,name,race_date):
        self.name=name
        self.date=race_date

    """print the name and date"""
    def __str__(self):
        return f"{self.name} ({self.date.strftime('%d-%m-%Y')})"

    """Usubtract today from self.date to calculate the how  many days remain until the days """
    def days_until(self,today):
        return (self.date-today).days

    #Alternative  way to build a rae object directly from a raw string 
    @classmethod
    def from_text(cls,text):

        #it's pattern to findout the string 
        #  (.+?) -> group of every char like uppercase lowenrcase etc 
        # \s+on\s+ -> means space and on then space 
        # (\d{2}-\d{2}-\d{4})-> group of date foramte (DD-MM-YYYY)
        match=re.fullmatch(r"(.+?)\s+on\s+(\d{2}-\d{2}-\d{4})",text.strip())


        #  if pattern are didnot match so raise a  valueError
        if not match:
            raise ValueError(f"Invalid formate : {text}")

        # unpacke the two  captured pieces into name and date_str
        name,date_str=match.groups()

        #straptime is autiomatically raise valueerror for impossible dates like 32-09-2026

        race_date=datetime.strptime(date_str,"%d-%m-%Y").date()
        return cls(name,race_date)

lines = [
    "Dutch GP on 06-09-2026",
    "Italian GP on 13-09-2026",
    "Spanish GP on 32-09-2026",      # not a real date
    "Singapore GP - 2026"            # wrong format
]

#storing the  valid race value 
valid_race=[]
#counting skipped calue 
skipped=0


#Parsing and error handling
"loop throught all 4 lines string one by one"
for line in lines:

    # """usign try and except value to use if valid_race so append text line if not so counting skipped"""
    try:
        valid_race.append(Race.from_text(line))
    except ValueError:
        skipped +=1

print(f"valid races :{len(valid_race)}")
print(f"Skipped: {skipped}")

# With `filter()` keep only the races after `today = date(2026, 9, 1)`, and with `reduce()` pick the earliest one.

# One valid race are collected the scripts find which one  happend next after 1 sept ,20265
today=date(2026, 9, 1)
# check every race r  in valid_race and keep only those  where r.days_until(today) > 0
upcoming=list(filter(lambda r:r.days_until(today) > 0, valid_race))

if upcoming :

    # Takes the upcoming race and compare them two into at a time (a and b)  
    next_race=reduce(lambda a,b :a if a.date < b.date else b ,upcoming)
    days_awys=next_race.days_until(today)
    summery=f"Next race:{next_race.name}({days_awys} days away)"
    print(summery)


    # folder  name
    folder="season"

    #create a new folder name  exist_ok=True -> if folder already exist so run 
    os.makedirs(folder,exist_ok=True)
    #join the file name in folder 
    file_path=os.path.join(folder,"next_race.txt")

    
    with open(file_path,"w")as f:
        f.write(summery + "\n")

    print("save seasion/next_race.txt")    