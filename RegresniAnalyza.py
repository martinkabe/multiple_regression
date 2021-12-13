from typing import List
from Matrix import Matice
from MatrixCalc import MatrixCustom

class Regrese:

    @classmethod
    def oddel_prediktory(cls, mat: Matice) -> List:
        dim_mat = mat.dimenze
        mat_bckp = MatrixCustom.matice_deep_copy(mat)
        y = []
        for r in range(dim_mat[0]):
            y_radek = []
            for s in range(dim_mat[1]):
                if s == 0:
                    y_radek.append(mat_bckp.data[r][s])
                    mat_bckp.data[r][s] = 1
            y.append(y_radek)
        y_mat = Matice(y)

        y_mat.sloupce = [mat.sloupce[0]]
        mat_bckp.sloupce = mat.sloupce[1:]
        y_mat.radky = mat_bckp.radky = mat.radky

        return(y_mat, mat_bckp)
