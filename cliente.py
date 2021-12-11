import json
class Cliente:
    def __init__(self):
        self.Clientes={}

    def registrar_cliente(self, nome, telefone, cidade):
        if nome not in self.Clientes:
            self.Clientes[nome]={"Telefone": telefone, "Cidade": cidade, "Pendentes": {}, "Total": 0.0}
        else:
            raise KeyError('Valor já está ná listá')

    def salvar(self):
        with open('cliente.json', 'w', encoding='utf8') as arq:
            json.dump(self.Clientes, arq, ensure_ascii=False, indent=4, separators=(',', ':'))
    
    def carregar(self):
        with open('cliente.json', 'r', encoding='utf8') as arq:
            ar=json.load(arq)
        self.Clientes=ar
