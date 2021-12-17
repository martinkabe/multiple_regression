from typing import List
from Matrix import Matice

class MatrixCustom:
    
    @classmethod
    def vynasob(cls, mat1: Matice, mat2: Matice) -> Matice:

        if isinstance(mat1.data, float) and any(isinstance(el, list) for el in mat2.data) or \
           isinstance(mat2.data, float) and any(isinstance(el, list) for el in mat1.data):
           # nasobeni matice konstantou
           konst = mat1.data if isinstance(mat1.data, float) else mat2.data
           mat = mat2 if isinstance(mat1.data, float) and any(isinstance(el, list) for el in mat2.data) else mat1
           mat_dim = mat.dimenze
           
           mat_vysledna = []
           for r in range(mat_dim[0]):
               radek_list = []
               for sl in range(mat_dim[1]):
                   radek_list.append(konst * mat.data[r][sl]) 
               mat_vysledna.append(radek_list)
           return(Matice(mat_vysledna))

        # Nasobeni matice s matici
        dim_mat1 = mat1.dimenze
        dim_mat2 = mat2.dimenze

        n_radku_mat1 = dim_mat1[0]
        n_sloupcu_mat1 = dim_mat1[1]
        n_sloupcu_mat2 = dim_mat2[1]

        if not any(isinstance(el, list) for el in mat1.data) and \
           not any(isinstance(el, list) for el in mat2.data):
           raise TypeError(f"Jedna z matic neni zadana jako List[List].")
        
        if dim_mat1[1] != dim_mat2[0]:
            raise TypeError(f"Matice 1 ma {dim_mat1[1]} sloupcu a matice 2 ma {dim_mat2[0]} radku, tedy ruzne dimenze.")

        mat_vysledna = []
        for m1_r in range(n_radku_mat1):
            radek_list = []
            for m2_s in range(n_sloupcu_mat2):
                sum = 0
                for m1_s in range(n_sloupcu_mat1):
                    sum += mat1.data[m1_r][m1_s] * mat2.data[m1_s][m2_s]
                radek_list.append(sum)
            mat_vysledna.append(radek_list)
        return(Matice(mat_vysledna))
    
    @classmethod
    def secti(cls, mat1: Matice, mat2: Matice) -> Matice:
        dim_mat1 = mat1.dimenze
        dim_mat2 = mat2.dimenze

        if not any(isinstance(el, list) for el in mat1.data) and \
           not any(isinstance(el, list) for el in mat2.data):
           raise TypeError(f"Jedna z matic neni zadana jako List[List].")
        
        if dim_mat1[0] != dim_mat2[0] or dim_mat1[1] != dim_mat2[1]:
            raise TypeError("Matice 1 ma rozmer ({dim_mat1[0]} x {dim_mat1[1]}), \
                             matice 2 ma rozmer ({dim_mat2[0]} x {dim_mat2[1]}).")
        
        mat_vysledna = []
        for r in range(dim_mat1[0]):
            radek_list = []
            for sl in range(dim_mat1[1]):
                radek_list.append(mat1.data[r][sl] + mat2.data[r][sl])
            mat_vysledna.append(radek_list)
        return(Matice(mat_vysledna))
    
    @classmethod
    def odecti(cls, mat1: Matice, mat2: Matice) -> Matice:
        dim_mat1 = mat1.dimenze
        dim_mat2 = mat2.dimenze

        if not any(isinstance(el, list) for el in mat1.data) and \
           not any(isinstance(el, list) for el in mat2.data):
           raise TypeError(f"Jedna z matic neni zadana jako List[List].")
        
        if dim_mat1[0] != dim_mat2[0] or dim_mat1[1] != dim_mat2[1]:
            raise TypeError("Matice 1 ma rozmer ({dim_mat1[0]} x {dim_mat1[1]}), \
                             matice 2 ma rozmer ({dim_mat2[0]} x {dim_mat2[1]}).")
        
        mat_vysledna = []
        for r in range(dim_mat1[0]):
            radek_list = []
            for sl in range(dim_mat1[1]):
                radek_list.append(mat1.data[r][sl] - mat2.data[r][sl])
            mat_vysledna.append(radek_list)
        return(Matice(mat_vysledna))
    
    @classmethod
    def transpozice(cls, mat: Matice) -> Matice:

        if not any(isinstance(el, list) for el in mat.data):
           raise TypeError(f"Matice neni zadana jako List[List].")

        mat_dim = mat.dimenze

        mat_vysledna = []
        for sl in range(mat_dim[1]):
            radek_list = []
            for r in range(mat_dim[0]):
                radek_list.append(mat.data[r][sl])
            mat_vysledna.append(radek_list)
        return(Matice(mat_vysledna))

    @classmethod
    def shodnost_matic(cls, mat1: Matice, mat2: Matice, tol=None) -> bool:

        dim_mat1 = mat1.dimenze
        dim_mat2 = mat2.dimenze

        if not any(isinstance(el, list) for el in mat1.data) and \
           not any(isinstance(el, list) for el in mat2.data):
           raise TypeError(f"Jedna z matic neni zadana jako List[List].")
        
        if dim_mat1[0] != dim_mat2[0] or dim_mat1[1] != dim_mat2[1]:
            raise TypeError("Matice 1 ma rozmer ({dim_mat1[0]} x {dim_mat1[1]}), \
                             matice 2 ma rozmer ({dim_mat2[0]} x {dim_mat2[1]}).")

        for r in range(dim_mat1[0]):
            for sl in range(dim_mat1[1]):
                if tol is None:
                    if mat1.data[r][sl] != mat2.data[r][sl]:
                        return False
                else:
                    if round(mat1.data[r][sl], tol) != round(mat2.data[r][sl], tol):
                        return False
        return True
    
    @classmethod
    def matice_deep_copy(cls, mat: Matice) -> Matice:

        if not any(isinstance(el, list) for el in mat.data):
           raise TypeError(f"Matice neni zadana jako List[List].")

        return Matice(mat.data)
    
    @classmethod
    def nulova_matice(cls, radky: int, sloupce: int) -> Matice:

        if not isinstance(radky, int) or not isinstance(sloupce, int):
            raise TypeError("Radek nebo sloupec neni zadan jako celociselna hodnota.")

        nul_mat = []
        for r in range(radky):
            nul_mat.append([0.0] * sloupce)
        return Matice(nul_mat)
    
    @classmethod
    def jednotkova_matice(cls, n: int) -> Matice:

        if not isinstance(n, int):
           raise TypeError(f"Rozmer jednotkove matice musi byt zadan jako celociselna hodnota.")
        
        mat_nul = cls.nulova_matice(n, n).data
        for r in range(n):
            mat_nul[r][r] = 1.0
        return Matice(mat_nul)
    
    @classmethod
    def skalarni_soucin(cls, mat1: Matice, mat2: Matice) -> float:

        dim_mat1 = mat1.dimenze
        dim_mat2 = mat2.dimenze

        if dim_mat1[0] != dim_mat2[0] or dim_mat1[1] != dim_mat2[1]:
            raise TypeError("Matice 1 ma rozmer ({dim_mat1[0]} x {dim_mat1[1]}), \
                             matice 2 ma rozmer ({dim_mat2[0]} x {dim_mat2[1]}).")
        
        celkem = 0
        for r in range(dim_mat1[0]):
            for sl in range(dim_mat2[1]):
                celkem += mat1.data[r][sl] + mat2.data[r][sl]
        return celkem
    
    @classmethod
    def determinant_rekurzivne(cls, mat: Matice, celkem: int = 0) -> float:
        indx = list(range(len(mat.data)))
        mat_dim = mat.dimenze
        # base case: matice 2x2
        if mat_dim[0] == mat_dim[1] == 2:
            hodnota = mat.data[0][0] * mat.data[1][1] - mat.data[1][0] * mat.data[0][1]
            return hodnota
        
        for sl in indx:
            mat_data_cpy = cls.matice_deep_copy(mat)
            mat_data_cpy.data = mat_data_cpy.data[1:] # odstran 1. radek
            sl_zbyvajici = len(mat_data_cpy.data)

            for i in range(sl_zbyvajici):
                mat_data_cpy.data[i] = mat_data_cpy.data[i][0:sl] + mat_data_cpy.data[i][sl+1:]

            znamenko = (-1) ** (sl % 2)
            sub_det = cls.determinant_rekurzivne(mat_data_cpy)
            celkem += znamenko * mat.data[0][sl] * sub_det
        
        return celkem
    
    @classmethod
    def singularita(cls, mat: Matice):
        det = cls.determinant_rekurzivne(mat)
        if det == 0:
            raise ArithmeticError("Singularni matice.")
    
    @classmethod
    def ctvercovost(cls, mat: Matice):
        mat_dim = mat.dimenze
        if mat_dim[0] != mat_dim[1]:
            raise ArithmeticError("Matice neni ctvercova")
    
    @classmethod
    def inverzni_matice(cls, mat: Matice, tol=None) -> Matice:

        # nejprve otestuji, jestli je matice ctvercova a neni singularni
        cls.ctvercovost(mat)
        cls.singularita(mat)

        mat_dim = mat.dimenze

        n = mat_dim[0]
        matM = cls.matice_deep_copy(mat)
        I = cls.jednotkova_matice(n)
        IM = cls.matice_deep_copy(I)

        indices = list(range(n))
        for fd in range(n):
            fdScaler = 1.0 / matM.data[fd][fd]
            
            for j in range(n):
                matM.data[fd][j] *= fdScaler
                IM.data[fd][j] *= fdScaler
            
            for i in indices[0:fd] + indices[fd+1:]: 
                
                crScaler = matM.data[i][fd]
                for j in range(n): 
                    matM.data[i][j] = matM.data[i][j] - crScaler * matM.data[fd][j]
                    IM.data[i][j] = IM.data[i][j] - crScaler * IM.data[fd][j]

        # test oproti jednotkove matici s urcitou toleranci v desetinnem miste
        if cls.shodnost_matic(I, cls.vynasob(mat, IM), tol):
            return IM
        else:
            raise ArithmeticError("Inverzni matice je mimo desetinnou toleranci.")
    
    @classmethod
    def extrakce_diagonaly(cls, mat: Matice) -> List:
        mat_dim = mat.dimenze
        diag = []
        for r in range(mat_dim[0]):
            for sl in range(mat_dim[1]):
                if r==sl:
                    diag.append(mat.data[r][sl])
        return diag



# m3 = Matice([[1,4,3], [4,5,6], [7,8,9]])
# m3_inverze = MatrixCustom.inverzni_matice(m3, 3)
# print("")

# det_m3 = MatrixCustom.determinant_rekurzivne(m3)
# print("")

# jedn_matice = MatrixCustom.jednotkova_matice(3)
# print("")

# m1 = Matice([[1,2], [3,4]], [1,2])
# print(m1.dimenze)
# m2 = Matice([[1,2,3], [4,5,6]], [1,2])
# print(m2.dimenze)
# m_konst = Matice(5)

# m3 = Matice([[1,2,3], [4,5,6], [7,8,9]])
# m4 = Matice([[1,2,3], [4,5,6], [7,8,9]])
# print(MatrixCustom.transpozice([[1,2,3], [4,5,6], [7,8,9]]))

# print(MatrixCustom.vynasob([[1,2,3], [4,5,6]], 5))

# print(MatrixCustom.vynasob(m_konst, m2))

# mat_soucet = MatrixCustom.secti(m3, m4)
# print(mat_soucet)
# print(mat_soucet.data)

# print(MatrixCustom.odecti([[2,4,6], [8,10,12], [14,16,18]],
#                           [[1,2,3], [4,5,6], [7,8,9]]))
