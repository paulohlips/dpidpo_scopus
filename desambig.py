import pandas as pd
import numpy as np
import csv
import json


lattes_table = list()  # vetor nome,[variações]
line_dataframe = list()
author_vector = list()
match = 0
notMatch = 0

n = j = 0

# Importa arquivo .csv e converte em dataframe
lattes_csv = pd.read_csv('./csv/lattes.csv')
scopus_csv = pd.read_csv('./csv/scopus.csv')

scopus = pd.DataFrame(scopus_csv)

lattes_df = pd.DataFrame(lattes_csv)
lattes = lattes_df.drop(["Currículo Lattes"], axis=1)


# Desmebra a coluna de "Authors" e cria um vetor com os autores
for line in scopus["Authors"]:
    authors = line.split(',')
    for author in authors:
        author_vector.append(author)

# Desmebra a coluna com as variações de nome e cria um vetor com elas
for line in lattes["Nome em Citações Bibliográficas"]:
    lattes_vector = list()
    aux_vec = list()

    authors = line.split(';')
    for name in authors:
        lattes_vector.append(name)
    lattes_table.append([lattes.iloc[[n], [0]].to_string(
        header=False, index=False), lattes_vector]),
    n += 1

x = 'paulo'
y = ["paulo", 'henrique']
# Faz a desambiguação com base no lattes

for author in author_vector:
    for i in range(0, len(lattes_table)):
        # if any(word in author for word in lattes_table[i][1]):
        for name in lattes_table[i][1]:
            if author == name:
                match += 1
                print(author, name)
            else:
                notMatch += 1
                print(author, name)


print(j, match, notMatch)


""" f = open("./csv/data_frame_lattes.csv", "w")
with f:
    writer = csv.writer(f)
    for row in lattes_vector:
        writer.writerow(row)
 """
