import math
from typing import List
from Matrix import Matice
from MatrixCalc import MatrixCustom as mc
from scipy.stats import t


class Regrese:

    @classmethod
    def oddel_prediktory(cls, mat: Matice) -> List:
        dim_mat = mat.dimenze
        mat_bckp = mc.matice_deep_copy(mat)
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
        mat_bckp.sloupce.insert(0, 'Intercept')
        y_mat.radky = mat_bckp.radky = mat.radky

        return(y_mat, mat_bckp)
    
    @classmethod
    def vypocti_odhady_koeficientu(cls, data: Matice) -> Matice:
        y, X = cls.oddel_prediktory(data)

        XT = mc.transpozice(X)
        XTX = mc.vynasob(XT, X)
        XTX_inv = mc.inverzni_matice(XTX, 2)

        XTy = mc.vynasob(XT, y)
        b = mc.vynasob(XTX_inv, XTy)
        b.sloupce = koef_nazvy = X.sloupce

        y1 = mc.transpozice(mc.odecti(y, mc.vynasob(X, b)))
        y2 = mc.odecti(y, mc.vynasob(X, b))
        dSigmaSq = Matice(mc.vynasob(y1, y2).data[0][0] / (X.dimenze[0] - b.dimenze[0]))
        dSigmaSq_XTX_inv = mc.vynasob(dSigmaSq, XTX_inv)

        sd_koeficienty = [math.sqrt(i) for i in mc.extrakce_diagonaly(dSigmaSq_XTX_inv)]
        b_odhady = [item for sublist in b.data for item in sublist]

        testova_kriteria = [i / j for i, j in zip(b_odhady, sd_koeficienty)]

        p_hodnoty = [2 * (1 - t.cdf(abs(tk), X.dimenze[0] - b.dimenze[0])) for tk in testova_kriteria]

        return(koef_nazvy, b_odhady, sd_koeficienty, testova_kriteria, p_hodnoty)

