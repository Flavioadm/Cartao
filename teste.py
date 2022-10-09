import csv

with open("visa.csv", "r") as arquivo:
    verificacao = csv.reader(arquivo, delimiter = ",")
    for linha in verificacao:
        print(linha)
