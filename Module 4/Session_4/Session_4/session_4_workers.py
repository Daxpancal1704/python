"""Helper functions for Session 4 - Multiprocessing.

Why does this file exist?
On Windows (and on macOS) multiprocessing starts every child process with a
fresh Python interpreter ("spawn"). The child has to *import* the function it
should run. Functions written inside a Jupyter notebook cell cannot be
imported, so they cannot be used as process targets. Keeping the worker
functions in a normal .py module solves that.

Note: print() inside a child process usually does NOT show up in the notebook
(it goes to the terminal that started Jupyter). That is why these workers send
their results back with a return value, a Queue, a Pipe or shared memory.
"""
import os
import time

squad = []  # used to show that processes do NOT share memory


# ---------- simple work functions ----------
def cpu_heavy(n):
    """CPU-bound work: a pure-Python loop that only calculates (no waiting).
    Think of it as crunching the statistics of n deliveries."""
    total = 0
    for i in range(n):
        total += i * i
    return total


def square(x):
    return x * x


def power(base, exp):
    return base ** exp


def which_process(x):
    """Returns the number together with the id of the process that handled it."""
    time.sleep(0.2)
    return x, os.getpid()


def may_fail(match_no):
    if match_no == 3:
        raise ValueError(f"Scorecard of match {match_no} is corrupted")
    return f"Scorecard of match {match_no} OK"


# ---------- Process + Queue ----------
def report_pid(name, q):
    q.put(f"{name} ran in process {os.getpid()} (parent {os.getppid()})")


def add_to_squad(player):
    squad.append(player)  # in a new process this changes only that process's own copy


def send_scores(q, scores):
    for runs in scores:
        time.sleep(0.1)  # pretend producing each score takes time
        q.put(runs)
    q.put(None)  # sentinel: "nothing more is coming"


# ---------- Pipe ----------
def third_umpire(conn):
    """Receives review requests and sends back a decision until it gets 'close'."""
    decisions = {"lbw": "OUT", "run out": "NOT OUT", "catch": "OUT"}
    while True:
        request = conn.recv()
        if request == "close":
            conn.send("Third umpire signing off")
            break
        conn.send(decisions.get(request, "UMPIRE'S CALL"))
    conn.close()


# ---------- Value / Array ----------
def add_runs_unsafe(total, times):
    for _ in range(times):
        total.value += 1  # read + write are two steps -> race condition


def add_runs_safe(total, times):
    for _ in range(times):
        with total.get_lock():  # only one process at a time
            total.value += 1


def double_runs(arr):
    for i in range(len(arr)):
        arr[i] *= 2


# ---------- Manager ----------
def record_innings(scores, batting_order, name, runs):
    scores[name] = runs
    batting_order.append(name)
