from Matrix import Matice

class MatrixCustom:
    
    @classmethod
    def vynasob(cls, mat1: Matice, mat2: Matice) -> Matice:

        if isinstance(mat1.data, int) and any(isinstance(el, list) for el in mat2.data) or \
           isinstance(mat2.data, int) and any(isinstance(el, list) for el in mat1.data):
           # nasobeni matice konstantou
           konst = mat1.data if isinstance(mat1.data, int) else mat2.data
           mat = mat2 if isinstance(mat1.data, int) and any(isinstance(el, list) for el in mat2.data) else mat1
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

        if dim_mat1[0] != dim_mat2[0] or dim_mat1[1] != dim_mat2[1]:
            raise TypeError("Matice 1 ma rozmer ({dim_mat1[0]} x {dim_mat1[1]}), \
                             matice 2 ma rozmer ({dim_mat2[0]} x {dim_mat2[1]}).")
        
        if not any(isinstance(el, list) for el in mat1.data) and \
           not any(isinstance(el, list) for el in mat2.data):
           raise TypeError(f"Jedna z matic neni zadana jako List[List].")
        
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

        if dim_mat1[0] != dim_mat2[0] or dim_mat1[1] != dim_mat2[1]:
            raise TypeError("Matice 1 ma rozmer ({dim_mat1[0]} x {dim_mat1[1]}), \
                             matice 2 ma rozmer ({dim_mat2[0]} x {dim_mat2[1]}).")
        
        if not any(isinstance(el, list) for el in mat1.data) and \
           not any(isinstance(el, list) for el in mat2.data):
           raise TypeError(f"Jedna z matic neni zadana jako List[List].")
        
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


m1 = Matice([[1,2], [3,4]], [1,2])
# print(m1.dimenze)
m2 = Matice([[1,2,3], [4,5,6]], [1,2])
# print(m2.dimenze)
m_konst = Matice(5)

m3 = Matice([[1,2,3], [4,5,6], [7,8,9]])
m4 = Matice([[1,2,3], [4,5,6], [7,8,9]])
# print(MatrixCustom.transpozice([[1,2,3], [4,5,6], [7,8,9]]))

# print(MatrixCustom.vynasob([[1,2,3], [4,5,6]], 5))

# print(MatrixCustom.vynasob(m_konst, m2))

mat_soucet = MatrixCustom.secti(m3, m4)
print(mat_soucet)
print(mat_soucet.data)

# print(MatrixCustom.odecti([[2,4,6], [8,10,12], [14,16,18]],
#                           [[1,2,3], [4,5,6], [7,8,9]]))
