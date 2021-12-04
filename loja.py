#dict_={'Peça': 'Carenagem', 'Modelo': 'Titan 150', 'Preço': 12.00, 'Partileira': 3}
import json as js
from typing import ParamSpecKwargs
class Loja:
    def __init__(self):
        self.List={}
        self.pendentes=[]

    def registrar_peca(self, Peca, Modelo, Preco, Total, Partileira, Mao_D_O):
        if Peca in self.List:
            raise NameError('Item já está na lista')
        else:
            self.List[Peca]={'Modelo': Modelo, 'Preço': Preco, 'Total': Total,'Partileira': Partileira, 'Mão de obra': Mao_D_O}

                
    def carregar(self):
        self.List.clear()
        with open('pecas.json', 'r', encoding='utf8') as arq:
            self.List=js.load(arq)
    
    def salvar(self):
        with open('pecas.json', 'w', encoding='utf8') as arq:
            js.dump(self.List, arq, ensure_ascii=False, indent=4, separators=(',', ':'))


if __name__=='__main__':
    from os import system as sy
    lj=Loja()

    lj.registrar_peca('X', 'X', 'X', 'X', 'X', 'X')
    #lj.registrar_peca('X', 'X', 'X', 'X', 'X', 'X')
    print(lj.List)
