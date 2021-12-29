import math
from typing import List, Tuple
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
        try:
            y, X = cls.oddel_prediktory(data)

            XT = mc.transpozice(X)
            XTX = mc.vynasob(XT, X)
            XTX_inv = mc.inverzni_matice(XTX, 2)

            XTy = mc.vynasob(XT, y)
            b = mc.vynasob(XTX_inv, XTy)
            b.sloupce = koef_nazvy = X.sloupce

            if (X.dimenze[0]-1) <= b.dimenze[0]:
                raise ArithmeticError(f"Pocet pozorovani je jen {X.dimenze[0]} a pocet regresnich koeficientu je {b.dimenze[0]}. Je potreba pridat vice pozorovani!")

            rsquares = cls.r_squares(y, X, b)

            y1 = mc.transpozice(mc.odecti(y, mc.vynasob(X, b)))
            y2 = mc.odecti(y, mc.vynasob(X, b))
            
            dSigmaSq = Matice(mc.vynasob(y1, y2).data[0][0] / (X.dimenze[0] - b.dimenze[0]))
            dSigmaSq_XTX_inv = mc.vynasob(dSigmaSq, XTX_inv)

            sd_koeficienty = [math.sqrt(i) for i in mc.extrakce_diagonaly(dSigmaSq_XTX_inv)]
            b_odhady = [item for sublist in b.data for item in sublist]

            testova_kriteria = [i / j for i, j in zip(b_odhady, sd_koeficienty)]

            p_hodnoty = [2 * (1 - t.cdf(abs(tk), X.dimenze[0] - b.dimenze[0])) for tk in testova_kriteria]

            return(koef_nazvy, b_odhady, sd_koeficienty, testova_kriteria, p_hodnoty, rsquares)
        except Exception as e:
            raise Exception("Trida 'Regrese' -> metoda 'vypocti_odhady_koeficientu': " + str(e))

    @classmethod
    def r_squares(cls, y: Matice, X: Matice, b: Matice) -> Tuple:
        ssr = sst = 0
        n = X.dimenze[0]
        k = b.dimenze[0]
        y_list = [item for sublist in y.data for item in sublist]
        predikce = mc.vynasob(X, b)
        predikce_list = [item for sublist in predikce.data for item in sublist]
        y_bar = cls.aritmeticky_prumer(y_list)

        for i in range(n):
            ssr += (y_list[i] - predikce_list[i])**2
            sst += (y_list[i] - y_bar)**2
        
        r_square = 1 - (ssr/sst)
        r_square_adj = 1 - (((1-r_square)*(n-1))/(n-k-1))

        return({"RSquare": r_square, "AdjRSquare": r_square_adj})

    
    @classmethod
    def aritmeticky_prumer(cls, x: List) -> float:
        sum = 0
        x_len = len(x)
        for i in range(x_len):
            sum += x[i]
        return(sum/x_len)
