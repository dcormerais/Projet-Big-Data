#!/usr/bin/env python
"""mapper_lot1.py"""

import sys
from datetime import datetime

for line in sys.stdin:
    line = line.strip()
    if line:
        columns = line.split(",")
        codecde = columns[6].strip('""')
        dept_str = columns[4].strip('""')
        ville = columns[5].strip('""')
        timbrecde = columns[9].strip('""')
        qte = columns[15].strip('""')
        if not dept_str.isdigit():
            continue

        dept = int(dept_str)
        date_str = columns[7].strip('""')
        start_date = datetime.strptime('2006-01-01', "%Y-%m-%d")
        end_date = datetime.strptime('2010-12-31', "%Y-%m-%d")

        try:
            if date_str.lower() in ('null', 'laval', 'vannes'):
                continue
            date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            if (start_date <= date <= end_date) and (dept // 1000 in (53, 61, 28)):
                print('%s\t%s\t%s\t%s\t%s\t%s' % (codecde,  ville, timbrecde, qte, date, dept // 1000))

        except ValueError:
            pass
