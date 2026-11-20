import multiprocessing
import os
import time

def play_matc(match,seconds):
    print(f"{match} started in process {os.getpid()}")
    time.sleep(seconds)
    print(f"{match} finsihed")

if __name__=="__main__":
    print("Main preocess id : ",os.getpid())
    p1=multiprocessing.Process(target=play_matc,args=("Ind vs aus ",1))
    p2=multiprocessing.Process(target=play_matc, args=("enf vs sa",1))

    start=time.perf_counter()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"Both matche done in {time.perf_counter() - start:.2f} s")
