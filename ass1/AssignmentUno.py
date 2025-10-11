import numpy as np
import math
import matplotlib as plt
import os
import time

start = time.time()

current_dir = os.path.dirname(__file__)  # cartella dove si trova lo script
file_path = os.path.join(current_dir, "frankenstein.txt")

# Apro e leggo tutto il contenuto del libro 
with open(file_path, "r", encoding="utf-8") as f: 
    testo = f.read()

class Lettera:
    def __init__(self, car):
        self._car = car    # underscore: attributo “interno” (non privato, ma convenzionalmente)

    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, nuovo_car):
        if not nuovo_car.strip():  #'strip' elimina gli spazi vuoti all'inizio e alla fine di una frase
            pass
        if nuovo_car > 0:
            pass
        if nuovo_car == 0:
            pass
        if nuovo_car < 0:
            pass
        self._car = nuovo_car
    
    def conta(self):
        return sum(1 for c in self._car)

    def saluta(self):
        print(f"Ciao, sono {self.car} e sono comparsa  volte.")


l_01 = Lettera("a")
l_02 = Lettera("A")
l_03 = Lettera("b")
l_04 = Lettera("B")
l_05 = Lettera("c")
l_06 = Lettera("C")
l_07 = Lettera("d")
l_08 = Lettera("D")
l_09 = Lettera("e")
l_10 = Lettera("E")
l_11 = Lettera("f")
l_12 = Lettera("F")
l_13 = Lettera("g")
l_14 = Lettera("G")
l_15 = Lettera("h")
l_16 = Lettera("H")
l_17 = Lettera("i")
l_18 = Lettera("I")
l_19 = Lettera("j")
l_20 = Lettera("J")
l_21 = Lettera("k")
l_22 = Lettera("K")
l_23 = Lettera("l")
l_24 = Lettera("L")
l_25 = Lettera("m")
l_26 = Lettera("M")
l_27 = Lettera("n")
l_28 = Lettera("N")
l_29 = Lettera("o")
l_30 = Lettera("O")
l_31 = Lettera("p")
l_32 = Lettera("P")
l_33 = Lettera("q")
l_34 = Lettera("Q")
l_35 = Lettera("r")
l_36 = Lettera("R")
l_37 = Lettera("s")
l_38 = Lettera("S")
l_39 = Lettera("t")
l_40 = Lettera("T")
l_41 = Lettera("u")
l_42 = Lettera("U")
l_43 = Lettera("v")
l_44 = Lettera("V")
l_45 = Lettera("x")
l_46 = Lettera("X")
l_47 = Lettera("y")
l_48 = Lettera("Y")
l_49 = Lettera("w")
l_50 = Lettera("W")
l_51 = Lettera("z")
l_52 = Lettera("Z")

l_01.conta()
l_02.conta()
l_03.conta()
l_04.conta()
l_05.conta()
l_06.conta()
l_07.conta()
l_08.conta()
l_09.conta()
l_10.conta()
l_11.conta()
l_12.conta()
l_13.conta()
l_14.conta()
l_15.conta()
l_16.conta()
l_17.conta()
l_18.conta()
l_19.conta()
l_20.conta()
l_21.conta()
l_22.conta()
l_23.conta()
l_24.conta()
l_25.conta()
l_26.conta()
l_27.conta()
l_28.conta()
l_29.conta()
l_30.conta()
l_31.conta()
l_32.conta()
l_33.conta()
l_34.conta()
l_35.conta()
l_36.conta()
l_37.conta()
l_38.conta()
l_39.conta()
l_40.conta()
l_41.conta()
l_42.conta()
l_43.conta()
l_44.conta()
l_45.conta()
l_46.conta()
l_47.conta()
l_48.conta()
l_49.conta()
l_50.conta()
l_51.conta()
l_52.conta()

l_01.saluta()
l_02.saluta()
l_03.saluta()
l_04.saluta()
l_05.saluta()
l_06.saluta()
l_07.saluta()
l_08.saluta()
l_09.saluta()
l_10.saluta()
l_11.saluta()
l_12.saluta()
l_13.saluta()
l_14.saluta()
l_15.saluta()
l_16.saluta()
l_17.saluta()
l_18.saluta()
l_19.saluta()
l_20.saluta()
l_21.saluta()
l_22.saluta()
l_23.saluta()
l_24.saluta()
l_25.saluta()
l_26.saluta()
l_27.saluta()
l_28.saluta()
l_29.saluta()
l_30.saluta()
l_31.saluta()
l_32.saluta()
l_33.saluta()
l_34.saluta()
l_35.saluta()
l_36.saluta()
l_37.saluta()
l_38.saluta()
l_39.saluta()
l_40.saluta()
l_41.saluta()
l_42.saluta()
l_43.saluta()
l_44.saluta()
l_45.saluta()
l_46.saluta()
l_47.saluta()
l_48.saluta()
l_49.saluta()
l_50.saluta()
l_51.saluta()
l_52.saluta()

print("Il numero totale di lettere è:", c.conta())

end = time.time()

print(f"Tempo Impiegato: {end - start:.4f} secondi")