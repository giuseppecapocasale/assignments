import matplotlib.pyplot as plt
import time
import os

# In questo primo assignment vogliamo implementare un algoritmo che estragga la frequenza relativa di ciascuna lettera 
# in un testo: nel nostro caso il celebre romanzo "Frankenstein; or, the modern Prometeus" di Mary Shelley. 


start = time.time()

current_dir = os.path.dirname(__file__)  # cartella dove si trova lo script
file_path = os.path.join(current_dir, "frankenstein.txt")



# Apro e leggo tutto il contenuto del libro 
with open(file_path, "r", encoding="utf-8") as f: 
    testo = f.read()
# with apre e chiude il file automaticamente una volta letto. f rappresenta il file una volta aperto


# Definiamo il dizionario "alfabeto" che ci servirà a contare tutte le lettere dell'alfabeto a partire dallo 0
alfabeto = {'a' : 0, 'b': 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0} 


# Adesso iniziamo a contare tutte le lettere nel testo: ogni volta che trova una lettera incrementa 
# il conteggio di 1
for i in testo:
    if i in ("a","A"):
        alfabeto['a'] += 1
    if i in ("b","B"):
        alfabeto['b'] += 1 
    if i in ("c","C"):
        alfabeto['c'] += 1
    if i in ("d","D"):
        alfabeto['d'] += 1
    if i in ("e","E"):
        alfabeto['e'] += 1
    if i in ("f","F"):
        alfabeto['f'] += 1
    if i in ("g","G"):
        alfabeto['g'] += 1 
    if i in ("h","H"):
        alfabeto['h'] += 1
    if i in ("i","I"):
        alfabeto['i'] += 1 
    if i in ("j","J"):
        alfabeto['j'] += 1
    if i in ("k","K"):
        alfabeto['k'] += 1
    if i in ("l","L"):
        alfabeto['l'] += 1
    if i in ("m","M"):
        alfabeto['m'] += 1
    if i in ("n","N"):
        alfabeto['n'] += 1 
    if i in ("o","O"):
        alfabeto['o'] += 1
    if i in ("p","P"):
        alfabeto['p'] += 1 
    if i in ("q","Q"):
        alfabeto['q'] += 1
    if i in ("r","R"):
        alfabeto['r'] += 1
    if i in ("s","S"):
        alfabeto['s'] += 1
    if i in ("t","T"):
        alfabeto['t'] += 1
    if i in ("u","U"):
        alfabeto['u'] += 1 
    if i in ("v","V"):
        alfabeto['v'] += 1
    if i in ("w","W"):
        alfabeto['w'] += 1 
    if i in ("x","X"):
        alfabeto['x'] += 1
    if i in ("y","Y"):
        alfabeto['y'] += 1
    if i in ("z","Z"):
        alfabeto['z'] += 1


# Adesso sommiamo tutti i values del dizionario in modo da estrarre il valore con cui normalizzare i conteggi
norma = sum(alfabeto.values())


# In questo ciclo sostituiamo il conteggio assoluto con la frequenza relativa (espressa in %) per ciascun value
for i in alfabeto:
    alfabeto[i] = alfabeto[i] * 100 / norma
        

# Adesso creo istogramma (grafico a barre) con le frequenze relative
# Ricordiamoci che plt.bar() vuole come argomento liste o arrays

plt.bar(list(alfabeto.keys()), list(alfabeto.values()), color = "skyblue", edgecolor = "black")

plt.title("Frequenza relativa delle lettere nel testo")
plt.xlabel("Lettere")
plt.ylabel("Frequenza %")

end = time.time()

print(f'Tempo impiegato = {end - start:.4f} secondi') 
# print() l'ho messo prima di show() sennò viene eseguito solo dopo che è stato chiuso il grafico creato con matplotlib
# io invece voglio che mi stampi subito il tempo. Per questo a volte ci diceva che il time era dell'ordine dei minuti


plt.show()



