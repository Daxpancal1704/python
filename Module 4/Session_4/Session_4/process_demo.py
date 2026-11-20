import multiprocessing
import os
import time

def play_match(match, seconds):
    print(f"{match} started in process {os.getpid()}")
    time.sleep(seconds)
    print(f"{match} finished")

if __name__ == "__main__":                       # <- only the main program runs this block
    print("Main process id:", os.getpid())
    p1 = multiprocessing.Process(target=play_match, args=("IND vs AUS", 1))
    p2 = multiprocessing.Process(target=play_match, args=("ENG vs SA", 1))

    start = time.perf_counter()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"Both matches done in {time.perf_counter() - start:.2f} s")
