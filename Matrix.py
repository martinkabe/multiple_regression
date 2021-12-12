from typing import List

class Matice:
    def __init__(self, data, radky: List = [], sloupce: List = []):
        self._data = data
        if not isinstance(sloupce, List):
            raise TypeError("Sloupce musi byt zadane jako List.")
        self._sloupce = sloupce
        if not isinstance(radky, List):
            raise TypeError("Radky musi byt zadane jako jako List.")
        self._radky = radky

    def __str__(self):
        return f"Objekt matice rozmeru {self.dimenze}. Pokud je rozmer None, tak se jedna o skalar."

    @property
    def data(self):
        return self._data
    
    @property
    def sloupce(self):
        return self._sloupce
    
    @property
    def radky(self):
        return self._radky
    
    @property
    def dimenze(self):
        return None if isinstance(self.data, int) else self.__dim(self.data)
    
    @data.setter
    def data(self, d: List):
        self._data = d
    
    @sloupce.setter
    def sloupce(self, s: List):
        self._sloupce = s
    
    @radky.setter
    def radky(self, r: List):
        self._radky = r

    def __dim(self, d: List[List]) -> List:
        if not type(d) == list:
            return []
        return [len(d)] + self.__dim(d[0])