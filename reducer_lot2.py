#!/usr/bin/env python
"""reducer_lot2.py"""
import sys
import decimal
from random import sample
import pandas as pd

# Fonction pour traiter une ligne de données et mettre à jour le dictionnaire commandes
def process_line(line, commandes):
    # Séparer les colonnes de la ligne
    columns = line.strip().split("\t")

    # Assurez-vous que la ligne a le bon format
    if len(columns) == 7:
        # Extraire les valeurs des colonnes
        key, ville, timbrecde, qte, date, dept, timbrecli = columns

        # Assurez-vous que la quantité est un nombre
        try:
            qte = int(qte)
            timbrecli = int(timbrecli)
        except ValueError:
            qte = 0
            timbrecli = 0

        # Mettre à jour le dictionnaire commandes
        if key not in commandes:
            commandes[key] = {"ville": ville, "qte_total": qte, "article_count": 1}
        else:
            commandes[key]["qte_total"] += qte
            commandes[key]["article_count"] += 1

# Dictionnaire pour stocker les commandes
commandes = {}

# Lecture de l'entrée standard
for line in sys.stdin:
    process_line(line, commandes)

# Triez le dictionnaire en fonction de la clé "qte"
sorted_commandes = sorted(
    commandes.items(), key=lambda x: x[1]["qte_total"], reverse=True
)

# On prend 5% des 100 meilleures commandes de façon aléatoire
command_selected = int(0.05 * 100)
meilleurs_commandes = sorted_commandes[:100]
selection_aleatoire = sample(meilleurs_commandes, command_selected)

# Créez un DataFrame à partir des données
mydata = []
for codcde, values in selection_aleatoire:
    ville = values["ville"]
    qte_total = values["qte_total"]
    article_count = values["article_count"]
    moy_commandes = qte_total / article_count if article_count > 0 else 0
    mydata.append([codcde, ville, qte_total, moy_commandes])

# Données à mettre dans le DataFrame
df = pd.DataFrame(
    mydata, columns=["Code Commande", "Ville", "Nb. Articles sans Timbre", "Moyennes Quantités de la Commande"]
)

# Enregistrez le DataFrame dans un fichier Excel
excel_file = "../BigData/lot2_exo1.xlsx"
df.to_excel(excel_file, index=False)
print(df)

