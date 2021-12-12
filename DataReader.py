import csv
from Matrix import Matice

class NactiData:
    
    @classmethod
    def data_do_matice(cls, cesta):
        rows = []
        row_num = 0
        with open(cesta, 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                rows.append(row)
                row_num += 1
        mat_out = Matice(rows, list(range(1, row_num + 1)), header)
        return(mat_out)


mat_test = NactiData.data_do_matice("Scripts/test/test1.csv")
print("")