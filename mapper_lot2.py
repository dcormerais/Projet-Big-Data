#!/usr/bin/env python
"""mapper_lot2.py"""

import sys
from datetime import datetime

for line in sys.stdin:
    line = line.strip()
    if line:
        columns = line.split(",")
        codecde = columns[6].strip('""')
        dept_str = columns[4].strip('""')
        ville = columns[5].strip('""')
        timbrecli = columns[8].strip('""')
        timbrecde = columns[9].strip('""')
        qte = columns[15].strip('""')
        if not dept_str.isdigit():
            continue

        dept = int(dept_str)
        date_str = columns[7].strip('""')
        start_date = datetime.strptime('2011-01-01', "%Y-%m-%d")
        end_date = datetime.strptime('2016-12-31', "%Y-%m-%d")

        try:
            if date_str.lower() in ('null', 'laval', 'vannes'):
                continue
            date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            if (start_date <= date <= end_date) and (dept // 1000 in (22, 49, 53)) and (timbrecli == '' or timbrecli == '0'):
                print('%s\t%s\t%s\t%s\t%s\t%s\t%s' % (codecde,  ville, timbrecde, qte, date, dept // 1000, timbrecli))

        except ValueError:
            pass
