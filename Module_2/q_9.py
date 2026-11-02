""""### Question 9 (Hard) - Log analyser with a generator pipeline
a) Generate a file `server.log` with **100,000** lines using a generator, for example:
`2026-10-27 14:03:22 | ERROR | payment | Timeout after 30s`
(levels `INFO / WARNING / ERROR`, a few services such as `auth`, `payment`, `search`, random times). Insert some **malformed** lines on purpose.

b) Build a **lazy pipeline** of generators, without ever loading the whole file into memory:
`read_lines(path)` -> `parse(lines)` (yields dicts; malformed lines are skipped and counted using `try/except`) -> `filter_level(records, level)`.

c) Using comprehensions / `Counter`, produce: number of records per level, the **set** of services that produced errors, and the hour of the day with the most errors.

d) Write all ERROR records to `errors.csv` with `csv.DictWriter` and a summary to `log_report.txt`.

e) Compare the memory of `f.readlines()` against your generator approach with `sys.getsizeof` and explain the result in a comment."""


import datetime  #Used to generate, parse, and structure human-readable timestamps.
import csv
import sys
import random  #Used to simulate real-world variance by picking random choices for errors, levels, and times.
from collections import Counter


#Genrated log file and line=100000
def genrated_log_file(filename="server.log",num_lines=100_000):
    """Generates a log file using straeming / writing line by line """
    levels=["INFO","WARNING","ERROR"]
    services=["auth","payment","search","users","checkout"]
    message={
        "INFO":["User logged in ","Search queary processd","cache hit"],
        "WARNING":["High latency detected","Rate limiting apporaching","Disk space 80%"],
        "ERROR":["Timeout after 30s","Database connnection faild ","Invalid token"]

    }
    # starting timeing
    start_time=datetime.datetime(2026,10,1)

    with open(filename,"w",encoding="utf-8")as f:
        for _ in range(num_lines):
            if random.random() < 0.01:
                f.write("MALFORMED_LINE_DATA_WITHOUT_PIPES_OR_VALID_TIMESTAMP\n") 
                continue
            #Advance randome time incremant up to few minutes
            
            start_time += datetime.timedelta(seconds=random.randint(1,180))
            timestemp_str=start_time.strftime("%Y-%m-%d %H:%M:%S")
            #find the random levels for levels
            level=random.choice(levels)
            #find service for service
            service=random.choice(services)
            #find mesg for randome level
            msg=random.choice(message[level])
            #it's formate for writeing 
            f.write(f"{timestemp_str} | {level} | {service} | {msg}\n ")


            #starting pipline 

def read_lines(path):
    """Generator: yields lines from the file one by one."""
    with open(path ,"r",encoding="utf-8")as file :
        for line in file:
            yield line

def parse(lines,malformed_counter_dict):
    """Generators : parse lines into dicts,skipping malformed once."""
    for line in lines:
        try:
            parts=[p.strip() for p in line.strip().split("|")]
            if len(parts) !=4:
                raise ValueError("Incorrect number of pipe-separeted fields")

            datetime.datetime.strptime(parts[0],"%Y-%m-%d %H:%M:%S")

            yield{
                "timestamp":parts[0],
                "level":parts[1],
                "service":parts[2],
                "message":parts[3]
            }
        except (ValueError,IndexError):
            malformed_counter_dict["count"] += 1


def filter_level(records,level):
    """Generator:fiters records by log level."""
    for record in records:
        if record["level"]==level:
            yield record

#main pipeline 
if __name__=="__main__":
    #log file store
    log_file="server.log"
    #calling function and use parameter calling 
    print("Genrateing log file...")
    genrated_log_file(log_file,100_000)
    print(f"log file '{log_file}' created successfully.\n")

    malform_tracker={"count":0}

    raw_lines=read_lines(log_file)
    parsed_record=parse(raw_lines,malform_tracker)

    #we consume the generator pipeline *once* to compute metrics and collect data
    level_counter=Counter()
    error_serivce=set()
    error_hours=[]
    error_record_save=[]

    for record in parsed_record:
        level_counter[record["level"]]+= 1

        if record['level']=="ERROR":
            error_serivce.add(record['service'])
            hour=record['timestamp'].split(" ")[1].split(":")[0]
            error_hours.append(hour)
            error_record_save.append(record)

    hour_counter=Counter(error_hours)
    peak_e_hour,peak_count=hour_counter.most_common(1)[0] if hour_counter else ("N/A",0)

    #Display Metrics
    print("___Analytics Summery____")
    print(f"record per leavle :{dict(level_counter)}")
    print(f"Malformed line skipped : {malform_tracker["count"]}")
    print(f"Serives with error: {error_serivce}")
    print(f"Peak Error Hour: {peak_e_hour}: 00 with {peak_count} error \n")


    #file error recorde to error.csv 

    with open("error.csv" ,"w",newline="",encoding="utf-8")as csvf:
        fieldnames=["timestamp","level","service","message"]
        writer=csv.DictWriter(csvf,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(error_record_save)

            #writer summery to log_report.txt

    with open("log_report.txt","w",encoding="utf-8")as  report:
        report.write("LOG ANALYSER REPORT SUMMERY\n..")
        report.write("_____________\n")
        report.write(f"Ttoal valid reocord processed : {sum(level_counter.values())}\n")
        report.write(f"Malformed lines : {malform_tracker['count']}\n\n")
        report.write(f"Breakdown by leavel\n")
        for levl,cnt in level_counter.items():
            report.write(f"   -{levl}:{cnt}\n")
        report.write(f"Seviece producing error: {',' .join(error_serivce)}\n ")
        report.write(f"hours of the with  most errors:{peak_e_hour}:00({peak_count} errors )\n ")
        
    with open(log_file,"r",encoding="utf-8")as f:
        listmemory=sys.getsizeof(f.readlines())
    
    genrated_memeory=sys.getsizeof(read_lines(log_file))

    print(f"Memory ovehead of f.readlines() list:{listmemory} bytes")
    print(f"Memeory overhead of readines() genrator : {genrated_memeory} bytes")
