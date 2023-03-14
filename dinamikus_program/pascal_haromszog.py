from math import factorial
from typing import List
class matematikai:
    u"""
    ide az egyszerű generálás jön n!/(k!(n-k)!) segítségével
    """
    n:int
    k:int
    def __init__(self,_n:int,_k:int) -> None:
        self.n = _n
        self.k = _k

    @property
    def nalattak(self):
        return factorial(self.n)/(factorial(self.k)*factorial(self.n - self.k))
    

class matharom:
    u"""
    a matematikai cuccból csinál háromszöget
    """
    data_tbl:List[matematikai]
    def __init__(self,sor:int) -> None:
        self.data_tbl = []
        for _sor in range(0,sor):
            temp_sor = []
            for _oszlop in range(0,_sor + 1):
                temp_sor.append(matematikai(_sor,_oszlop))
            self.data_tbl.append(temp_sor)

    def get_a_row(self, row) -> List[int]:
        return [x.nalattak for x in self.data_tbl[row]]

    @property
    def haromszog(self) ->str:
        rtn:str = ""
        for sor in range(0,len(self.data_tbl)):
            rtn = rtn + "\t".join([str(int(x)) for x in self.get_a_row(sor)]) + "\n"
        return rtn

class dinamikusan_klasszik(matharom):
    u"""
    na akkor most ugyan ezt a problémát járjuk be dinamikusan is
    """
    data_tbl:List[int]
    def __init__(self, sor:int) -> None:
        self.data_tbl = []
        for _sor in range(0,sor):
            temp_sor = []
            for oszlop in range(0,_sor + 1):
                if oszlop == 0 or _sor == oszlop:
                    temp_sor.append(1)
                else:
                    temp_sor.append(self.data_tbl[_sor - 1][oszlop - 1] + self.data_tbl[_sor - 1][oszlop])
            self.data_tbl.append(temp_sor)

    def get_a_row(self, row) -> List[int]:
        return [x for x in self.data_tbl[row]]

class rekurzivan(matharom):
    data_tbl:List[int]
    def __init__(self) -> None:
        self.data_tbl = []
        self.data_tbl.append([1])
        self.data_tbl.append([1, 1])

    def uj_elem(self, sor, oszlop) -> int:
        """ahhoz, hogy kiszámoljak 1 elemet az előző sorból 2 elem kell"""
        prev_sor = sor - 1 -1 
        prev_oszlop = [oszlop - 1 -1, oszlop - 1]
        if len(self.data_tbl) <= prev_sor + 1:
            for i in range(len(self.data_tbl), sor):
                temp_row = [1]
                for y in range(1,i):
                    temp_row.append(None)
                temp_row.append(1)
                self.data_tbl.append(temp_row)
        if prev_sor < len(self.data_tbl) and prev_oszlop[1] >= len(self.data_tbl[prev_oszlop[0]]) and self.data_tbl[prev_sor][prev_oszlop[0]] is not None and self.data_tbl[prev_sor][prev_oszlop[1]] is not None:
            self.data_tbl[sor -1 ][oszlop -1] = 0

        if self.data_tbl[prev_sor][prev_oszlop[0]] is None:
            self.uj_elem( prev_sor, oszlop-1)
        elif self.data_tbl[prev_sor][prev_oszlop[1]] is None:
            self.uj_elem(prev_sor, oszlop)



if __name__ == '__main__':
    elso = matematikai(5,2)
    print(elso.nalattak)
    math = matharom(8)
    print(math.get_a_row(3))
    print(math.haromszog)
    dp1 = dinamikusan_klasszik(8)
    print(dp1.haromszog)
    dp2 = rekurzivan()
    dp2.uj_elem(3,2)
    print(dp2.data_tbl)
    dp2.uj_elem(4,2)
    print(dp2.data_tbl)
    dp2.uj_elem(8,2)
    print(dp2.data_tbl)