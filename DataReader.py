import csv
from Matrix import Matice

class NactiData:
    
    @classmethod
    def data_do_matice(cls, cesta):
        rows = []
        with open(cesta, 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                rows.append(row)
        mat_out = Matice(rows)
        mat_out.radky = list(range(1, mat_out.dimenze[0] + 1))
        mat_out.sloupce = header
        return(mat_out)


mat_test = NactiData.data_do_matice("Scripts/test/test1.csv")
print("")