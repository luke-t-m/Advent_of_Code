#!/usr/bin/python3
import sys
from subprocess import run as subprocess_run
import heapq

def output(val):
    if val != 0:
        subprocess_run(["xsel", "--clipboard"], input=f"{val}".encode())
    print(val)





p1 = p2 = 0
inp = sys.argv[1]
directions = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}

numpad = dict()
numpad[(0, 1)] = 0
numpad[(0, 2)] = "A"
for i in range(9):
    at = (i // 3 + 1, i % 3)
    numpad[at] = str(i + 1)

keypad = {(0, 0) : "<", (0, 1): "v", (0, 2): ">", (1, 1): "^", (1, 2): "A"}
        


output(p1)
output(p2)