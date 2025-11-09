import argparse
import os
import string
import time

import matplotlib.pyplot as plt


# In questo primo assignment vogliamo implementare un algoritmo che estragga la frequenza relativa di ciascuna lettera 
# in un testo: nel nostro caso il celebre romanzo "Frankenstein; or, the modern Prometeus" di Mary Shelley. 

def process(file_path):

    start = time.time()

    assert file_path.endswith('.txt')
    assert os.path.isfile(file_path)

    # Apro e leggo tutto il contenuto del libro: with apre e chiude il file automaticamente una volta letto. input_file rappresenta il file una volta aperto
    with open(file_path, "r", encoding="utf-8") as input_file: 
        text = input_file.read()

    # Adesso iniziamo a contare tutte le lettere nel testo: ogni volta che trova una lettera incrementa il conteggio di 1
    counts_dict = {char: 0 for char in string.ascii_lowercase}
    for char in text.lower():
        if char in counts_dict:  # considera solo le lettere
            counts_dict[char] += 1

    # Adesso sommiamo tutti i values del dizionario in modo da estrarre il valore con cui normalizzare i conteggi
    norm_char = sum(counts_dict.values())
    
    # In questo ciclo sostituiamo il conteggio assoluto con la frequenza relativa (espressa in %) per ciascun value
    for char in counts_dict:
        counts_dict[char] = counts_dict[char] * 100 / norm_char

    # Adesso creo istogramma (grafico a barre) con le frequenze relative
    # Ricordiamoci che plt.bar() vuole come argomento liste o arrays
    plt.bar(list(counts_dict.keys()), list(counts_dict.values()), color = "skyblue", edgecolor = "black")
    plt.title("Relative frequency of the letters")
    plt.xlabel("Letters")
    plt.ylabel("Frequency %")

    end = time.time()
    print(f'Time spent = {end - start:.4f} seconds')

    plt.show()

    # print() l'ho messo prima di show() sennò viene eseguito solo dopo che è stato chiuso il grafico creato con matplotlib
    # io invece voglio che mi stampi subito il tempo. Per questo a volte ci diceva che il time era dell'ordine dei minuti


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This script counts the characters of a text file.")
    parser.add_argument('infile', help='path to the input file')
    args = parser.parse_args()
    process(args.infile)