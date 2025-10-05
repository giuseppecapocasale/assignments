import numpy as np
import math
import matplotlib as plt


testo = "Ciaoo, mi chiamo Giuseppe."

alfabeto = {"a": 0, "b": 0, "c":0, "d": 0, "e":0, "f": 0, "g":0, "h":0, "i":0, "j": 0, "k": 0, "l": 0, "m":0, "n": 0, "o":0, "p":0, "q": 0, "r": 0, "s":0, "t": 0, "u":0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

for i in testo:
    if i == "a" or i == "A":
        alfabeto["a"] += 1
    if i == "b" or i == "B":
        alfabeto["b"] += 1
    if i == "c" or i == "C":
        alfabeto["c"] += 1
    if i == "d" or i == "D":
        alfabeto["d"] += 1
    if i == "e" or i == "E":
        alfabeto["e"] += 1
    if i == "f" or i == "F":
        alfabeto["f"] += 1
    if i == "g" or i == "G":
        alfabeto["g"] += 1
    if i == "h" or i == "H":
        alfabeto["h"] += 1
    if i == "i" or i == "I":
        alfabeto["i"] += 1
    if i == "j" or i == "J":
        alfabeto["j"] += 1
    if i == "k" or i == "K":
        alfabeto["k"] += 1
    if i == "l" or i == "L":
        alfabeto["l"] += 1
    if i == "m" or i == "M":
        alfabeto["m"] += 1
    if i == "n" or i == "N":
        alfabeto["n"] += 1
    if i == "o" or i == "O":
        alfabeto["o"] += 1
    if i == "p" or i == "P":
        alfabeto["p"] += 1
    if i == "q" or i == "Q":
        alfabeto["q"] += 1
    if i == "r" or i == "R":
        alfabeto["r"] += 1
    if i == "s" or i == "S":
        alfabeto["s"] += 1
    if i == "t" or i == "T":
        alfabeto["t"] += 1
    if i == "u" or i == "U":
        alfabeto["u"] += 1
    if i == "v" or i == "V":
        alfabeto["v"] += 1
    if i == "w" or i == "W":
        alfabeto["w"] += 1
    if i == "x" or i == "X":
        alfabeto["x"] += 1
    if i == "y" or i == "Y":
        alfabeto["y"] += 1
    if i == "z" or i == "Z":
        alfabeto["z"] += 1


somma = sum(alfabeto.values())
print(somma)

for i in alfabeto:
    alfabeto[i] = alfabeto[i] * 100 / somma

print(alfabeto)
