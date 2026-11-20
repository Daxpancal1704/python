"Pool executors -> both pool and executors  helps  as run  multiple  tasks using multi processor and thread without manually creating every process or thread. "


# 1.What is pool in python
" pool is provider by the  mutliprocessing module"
" it creates a  group of worker processes. insetead of creating processes manually , you give task to the pool ,and it distributes the work among avilable workers."


import multiprocessing
import time

def square(number):
    print(f"processing {number}")


    time.sleep(2)
    return number * number

if __name__=="__main__":

    numbers=[1,2,3,4,5]
    
    with multiprocessing.Pool(processes=3)as pool:
        result=pool.map(square,numbers)
    print("result :",result)

