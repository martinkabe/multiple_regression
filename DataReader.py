import csv
from Matrix import Matice

class NactiData:
    
    @classmethod
    def data_do_matice(cls, cesta: str) -> Matice:
        rows = []
        row_num = 0
        with open(cesta, 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                rows.append([float(i) for i in row])
                row_num += 1
        return(Matice(rows, list(range(1, row_num + 1)), header))
