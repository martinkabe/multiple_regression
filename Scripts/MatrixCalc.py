from typing import List

class MatrixCustom:
    
    @classmethod
    def dim(cls, mat:List[List]) -> List:
        if not type(mat) == list:
            return []
        return [len(mat)] + cls.dim(mat[0])

    @classmethod
    def vynasob(cls, mat1: List[List], mat2: List[List]) -> List[List]:

        if isinstance(mat1, int) and any(isinstance(el, list) for el in mat2) or \
           isinstance(mat2, int) and any(isinstance(el, list) for el in mat1):
           # nasobeni matice konstantou
           konst = mat1 if isinstance(mat1, int) else mat2
           mat = mat2 if isinstance(mat1, int) and any(isinstance(el, list) for el in mat2) else mat1
           mat_dim = cls.dim(mat)
           
           mat_vysledna = []
           for r in range(mat_dim[0]):
               radek_list = []
               for sl in range(mat_dim[1]):
                   radek_list.append(konst * mat[r][sl]) 
               mat_vysledna.append(radek_list)
           return(mat_vysledna)

        dim_mat1 = cls.dim(mat1)
        dim_mat2 = cls.dim(mat2)

        n_radku_mat1 = dim_mat1[0]
        n_sloupcu_mat1 = dim_mat1[1]
        n_sloupcu_mat2 = dim_mat2[1]

        if not any(isinstance(el, list) for el in mat1) and \
           not any(isinstance(el, list) for el in mat2):
           raise TypeError(f"Jedna z matic neni zadana jako List[List].")
        
        if dim_mat1[1] != dim_mat2[0]:
            raise TypeError(f"Matice 1 ma {dim_mat1[1]} sloupcu a matice 2 ma {dim_mat2[0]} radku, tedy ruzne dimenze.")


        mat_vysledna = []
        for m1_r in range(n_radku_mat1):
            radek_list = []
            for m2_s in range(n_sloupcu_mat2):
                sum = 0
                for m1_s in range(n_sloupcu_mat1):
                    sum += mat1[m1_r][m1_s] * mat2[m1_s][m2_s]
                radek_list.append(sum)
            mat_vysledna.append(radek_list)
        return(mat_vysledna)
    
    @classmethod
    def secti(cls, mat1: List[List], mat2: List[List]) -> List[List]:
        dim_mat1 = cls.dim(mat1)
        dim_mat2 = cls.dim(mat2)

        if dim_mat1[0] != dim_mat2[0] or dim_mat1[1] != dim_mat2[1]:
            raise TypeError("Matice 1 ma rozmer ({dim_mat1[0]} x {dim_mat1[1]}), \
                             matice 2 ma rozmer ({dim_mat2[0]} x {dim_mat2[1]}).")
        
        if not any(isinstance(el, list) for el in mat1) and \
           not any(isinstance(el, list) for el in mat2):
           raise TypeError(f"Jedna z matic neni zadana jako List[List].")
        
        mat_vysledna = []
        for r in range(dim_mat1[0]):
            radek_list = []
            for sl in range(dim_mat1[1]):
                radek_list.append(mat1[r][sl] + mat2[r][sl])
            mat_vysledna.append(radek_list)
        return(mat_vysledna)
    
    @classmethod
    def odecti(cls, mat1: List[List], mat2: List[List]) -> List[List]:
        dim_mat1 = cls.dim(mat1)
        dim_mat2 = cls.dim(mat2)

        if dim_mat1[0] != dim_mat2[0] or dim_mat1[1] != dim_mat2[1]:
            raise TypeError("Matice 1 ma rozmer ({dim_mat1[0]} x {dim_mat1[1]}), \
                             matice 2 ma rozmer ({dim_mat2[0]} x {dim_mat2[1]}).")
        
        if not any(isinstance(el, list) for el in mat1) and \
           not any(isinstance(el, list) for el in mat2):
           raise TypeError(f"Jedna z matic neni zadana jako List[List].")
        
        mat_vysledna = []
        for r in range(dim_mat1[0]):
            radek_list = []
            for sl in range(dim_mat1[1]):
                radek_list.append(mat1[r][sl] - mat2[r][sl])
            mat_vysledna.append(radek_list)
        return(mat_vysledna)
    
    @classmethod
    def transpozice(cls, mat):

        if not any(isinstance(el, list) for el in mat):
           raise TypeError(f"Matice neni zadana jako List[List].")

        mat_dim = cls.dim(mat)

        mat_vysledna = []
        for sl in range(mat_dim[1]):
            radek_list = []
            for r in range(mat_dim[0]):
                radek_list.append(mat[r][sl])
            mat_vysledna.append(radek_list)
        return(mat_vysledna)



# print(MatrixCustom.transpozice([[1,2,3], [4,5,6], [7,8,9]]))

# print(MatrixCustom.vynasob([[1,2,3], [4,5,6]],
#                             5))

# print(MatrixCustom.vynasob([[1,2], [3,4]],
#                             [[1,2,3], [4,5,6]]))

# print(MatrixCustom.secti([[1,2,3], [4,5,6], [7,8,9]],
#                           [[1,2,3], [4,5,6], [7,8,9]]))

# print(MatrixCustom.odecti([[2,4,6], [8,10,12], [14,16,18]],
#                           [[1,2,3], [4,5,6], [7,8,9]]))
