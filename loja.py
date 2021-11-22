#dict_={'Peça': 'Carenagem', 'Modelo': 'Titan 150', 'Preço': 12.00, 'Partileira': 3}
import json as js
from typing import ParamSpecKwargs
class Loja:
    def __init__(self):
        self.List=[]
        self.pendentes=[]

    def registrar_peca(self, Peca, Modelo, Preco, Total, Partileira, Mao_D_O):
        pc={'Peça': Peca, 'Modelo': Modelo, 'Preço': Preco, 'Total': Total,'Partileira': Partileira, 'Mão de obra': Mao_D_O}

        for v in self.List:
            if v['Peça']==pc['Peça']:
                raise NameError('Item já está na lista')
        self.List.append(pc)
                
    def carregar(self):
        self.List.clear()
        with open('pecas.json', 'r', encoding='utf8') as arq:
            my_lits=js.load(arq)
        for c in my_lits:
            self.List.append(c)
    
    def salvar(self):
        with open('pecas.json', 'w', encoding='utf8') as arq:
            js.dump(self.List, arq, ensure_ascii=False, indent=4, separators=(',', ':'))


if __name__=='__main__':
    from os import system as sy
    lj=Loja()

    lj.registrar_peca('X', 'X', 'X', 'X', 'X', 'X')
    #lj.registrar_peca('X', 'X', 'X', 'X', 'X', 'X')
    print(lj.List)
