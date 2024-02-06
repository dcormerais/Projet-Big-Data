#!/usr/bin/env python3
"""reducer_lot1.py"""
import sys
import decimal
import pandas as pd

# Fonction pour traiter une ligne de données et mettre à jour le dictionnaire commandes
def process_line(line, commandes):
    # Séparer les colonnes de la ligne
    columns = line.strip().split("\t")

    # Assurez-vous que la ligne a le bon format
    if len(columns) == 6:
        # Extraire les valeurs des colonnes
        key, ville, timbrecde, qte, date, dept = columns

        # Assurez-vous que la quantité est un nombre
        try:
            qte = int(qte)
        except ValueError:
            qte = 0

        # Mettre à jour le dictionnaire commandes
        if key not in commandes:
            commandes[key] = {"ville": ville, "timbrecde": decimal.Decimal(timbrecde), "qte": qte}
        else:
            commandes[key]["qte"] += qte
            commandes[key]["timbrecde"] = max(commandes[key]["timbrecde"], decimal.Decimal(timbrecde))

# Dictionnaire pour stocker les commandes
commandes = {}

# Lecture de l'entrée standard
for line in sys.stdin:
    process_line(line, commandes)

# Triez le dictionnaire en fonction de la clé "qte"
sorted_commandes = sorted(
    commandes.items(), key=lambda x: (x[1]["qte"], x[1]["timbrecde"]),reverse=True
)

# Créez un DataFrame à partir des données
mydata = []
for codcde, values in sorted_commandes[:100]:
    mydata.append([codcde, values["ville"], values["qte"], values["timbrecde"]])

# Données à mettre dans le DataFrame
df = pd.DataFrame(mydata, columns=["codcde", "ville", "qte", "timbrecde"])

# Enregistrez le DataFrame dans un fichier Excel
df.to_excel("/datavolume1/lot1_exo1.xlsx", index=False)
