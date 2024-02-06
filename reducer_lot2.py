#!/usr/bin/env python
"""reducer_lot2.py"""
import sys
import decimal
from random import sample
import pandas as pd
import matplotlib.pyplot as plt

def process_line(line, commandes):
    columns = line.strip().split("\t")

    if len(columns) == 7:
        key, ville, timbrecde, qte, date, dept, timbrecli = columns

        try:
            qte = int(qte)
            timbrecli = int(timbrecli)
        except ValueError:
            qte = 0
            timbrecli = 0

        if key not in commandes:
            commandes[key] = {"ville": ville, "qte_total": qte, "article_count": 1}
        else:
            commandes[key]["qte_total"] += qte
            commandes[key]["article_count"] += 1

commandes = {}

for line in sys.stdin:
    process_line(line, commandes)

sorted_commandes = sorted(
    commandes.items(), key=lambda x: x[1]["qte_total"], reverse=True
)

command_selected = int(0.05 * 100)
meilleurs_commandes = sorted_commandes[:100]
selection_aleatoire = sample(meilleurs_commandes, command_selected)


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


df.to_excel("/datavolume1/lot2_exo1.xlsx", index=False)
print(df)

#df = pd.read_excel("/Users/gueye/Documents/test/lot2_test.xlsx")


plt.pie(df["Moyennes Quantités de la Commande"], labels=df["Ville"], autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Répartition des villes par rapport à la quantité')


plt.savefig('/datavolume1/PieChart01.pdf')
plt.show()


