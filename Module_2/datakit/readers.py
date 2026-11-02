
import csv
from pathlib import Path

from .errors import InvalidFileError


# converting string value to int and float


def convert_value(value):
    value=value.strip()

    if value == "":
        return None
    
    
    try:
        return int(value)
    except ValueError:
        pass

    
    try:
        return float(value)
    except ValueError:
        return value

#read value for path 

def read_rows(path):

    path=Path(path)

# .suffixuse the check file extenance means .csv it means check the file path .csv if not thr occurs the InvalidFileError

    if path.suffix.lower() != ".csv":
        raise InvalidFileError("File format is not CSV")

#DictReader use the read the file csv file for the csv foramate
    try:
        with path.open("r",newline="",encoding="utf-8")as file:
            reader=csv.DictReader(file,strict=True)


            if not reader.fieldnames:
                raise InvalidFileError("csv header is missing")
            
            if any(not name or not name.strip()):
                for name in reader.fildname():
                    raise InvalidFileError('Invalid coloumn name')

            if len(set(reader.fielnames)) != len(reader.fieldnames):
                raise InvalidFileError("Duplicate coloumn names")

            for row in reader:
                if None in row or any(v in None for v in row.values()):
                    raise InvalidFileError("Malform csv row")
    #       
                yield{
                    key:convert_value(value)
                    for key,value in row.items()
                }
    except InvalidFileError:
        raise 
    except (OSError,csv.Error,UnicodeError)as exc:
        raise InvalidFileError(
            f"Could not reasd.csv {exc}"

        )from exc
    

