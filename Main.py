from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from GUI import *
from sys import argv
from loja import *
from cliente import *

class Main(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.tot_gl=...
        self.nome_gl=...
        self.LJ=Loja()
        self.CL=Cliente()

        # Funções 1
        self.d_Exit()
        self.LJ.carregar()
        self.CL.carregar()
        # Funções 2
        self.R_pecas.clicked.connect(self.PR_pecas.show)
        self.BTT_peca.clicked.connect(self.d_registrar_pecas)
        self.Exit.clicked.connect(self.d_Exit)
        self.L_pecas.clicked.connect(self.listas_pecas)
        self.actionSalvar.triggered.connect(self.salvar)
        self.Ver_Detalhe.clicked.connect(self.event_PD)
        self.Excluir.clicked.connect(self.event_PE)
        self.BTT_A_Vista.clicked.connect(self.event_venda)
        self.R_cliente.clicked.connect(self.RE_Cliente.show)
        self.BTT_Rcliente.clicked.connect(self.d_registrar_cliente)
        self.R_conta.clicked.connect(self.listas_cliente)
        self.BTT_Detalhes.clicked.connect(self.event_detalhes)
        self.BTT_Fiado.clicked.connect(self.event_fiado)
        self.BTT_Pagar.clicked.connect(self.botao_pagar)
        #self.F_pedido.clicked.connect(self.PF_Pedidos.show)
        
    def d_registrar_pecas(self): # Terminar prenchimento de daods da peça
        msg='Este campo é obrigatorio!'
        prenchido=False

        v_pr=self.Preco.text().replace(' ', '').replace(',', '.')
        if v_pr=='':
            self.Preco.setPlaceholderText(msg)
            prenchido=True
            
        v_pe=self.Pecas.text()
        if v_pe=='':
            self.Pecas.setPlaceholderText(msg)
            prenchido=True

        v_mo=self.Mao_O.text().replace(' ', '').replace(',', '.')
        if v_mo=='':
            self.Mao_O.setPlaceholderText(msg)
            prenchido=True
        
        if prenchido:
            return ...
        else:
            try:
                md=self.M_D_Moto.text()
                tt=int(self.spinTot.text())
                pt=self.Part.text()

                self.LJ.registrar_peca(v_pe, md, float(v_pr), tt, pt, float(v_mo))
                self.d_Exit()

            except ValueError:
                self.popup('Estes valors não são valídos!', 'Valor invalído')

            except NameError:
                self.popup('Este item já está na lista', 'Item existente')

    def d_registrar_cliente(self):
        msg='Invalído!'
        prenchido=True
        px=self.C_Prefixo.currentText()

        nm=self.C_nome.text().capitalize().replace(' ', '')
        if nm=='':
            self.C_nome.setPlaceholderText(msg)
            prenchido=False

        tl=self.C_tel.text().replace(' ', '')
        if tl=='' and tl.isnumeric:
            self.C_tel.setPlaceholderText(msg)
            prenchido=False

        lg=self.C_lugar.text().replace(' ', '')
        if lg=='':
            self.C_lugar.setPlaceholderText(msg)
            prenchido=False

        if prenchido:
            try:
                self.CL.registrar_cliente(nm, f'({px}) {int(tl)}', lg)
                self.d_Exit()
            except KeyError:
                self.popup('Este nome já está registrado!', 'Já registrado')
            except ValueError:
                self.popup('Porfavor insira somente o número, sem nenhum tipo de caracter especial', 'Número invalído!') 

    def update_list_pecas(self):
        self.listPecas.clear()

        for k in self.LJ.List.keys():
            self.listPecas.addItem(k)

    def update_list_clientes(self):
        self.listDevendo.clear()
        self.Lista_de_pessoas.clear()

        for k in self.CL.Clientes.keys():
            self.listDevendo.addItem(k)
            self.Lista_de_pessoas.addItem(k)

    def d_Exit(self):
        self.PR_pecas.close()
        self.PR_pecas.close()
        self.PL_pecas.close()
        self.D_Pecas.close()
        self.RE_Cliente.close()
        self.PR_clients.close()
        self.Detalhe_cliente.close()
        #self.PF_Pedidos.close()

    def salvar(self):
        self.LJ.salvar()
        self.CL.salvar()

    def listas_pecas(self):
        self.PL_pecas.show() 
        self.update_list_pecas()
        self.listPecas.setCurrentRow(0)

    def listas_cliente(self):
        self.PR_clients.show()
        self.update_list_clientes()
        self.listDevendo.setCurrentRow(0)

    def event_PD(self):
        nome_peca=self.listPecas.currentItem().text()
        for k, v in self.LJ.List.items():
            if k==nome_peca:
                objeto_peca=v
                self.nome_gl=k
                break
        
        prc=objeto_peca["Preço"]
        self.D_Peca.setText(f'Peça: {self.nome_gl}')
        self.D_Modelo.setText(f'Modelo: {objeto_peca["Modelo"]}')
        self.D_Dispo.setText(f'Disponíveis: {objeto_peca["Total"]}')
        self.D_Preco.setText(f'Preço: {self.ConRS(prc)}')
        self.D_Part.setText(f'Partileira: {objeto_peca["Partileira"]}')
        self.tot_gl=self.ConRS(prc+objeto_peca["Mão de obra"])
        self.Dinhero_final.setText(f'Total: {self.ConRS(prc)}' if not self.CH_M_D_O.isChecked() else f'Total: {self.tot_gl}')

        self.update_list_clientes()
        self.Lista_de_pessoas.setCurrentRow(0)
        self.D_Pecas.show()

    def event_PE(self):
        nome_peca=self.listPecas.currentItem().text()
        indx_peca=self.listPecas.count()
        self.LJ.List.pop(nome_peca)
        self.listPecas.takeItem(indx_peca)
        self.update_list_pecas()

    def event_venda(self):
        nome_peca=self.listPecas.currentItem().text()
        if self.LJ.List[nome_peca]['Total']<=0:
            self.popup('Já não a mais peças disponiveis!', 'Esgotado')
        else:
            self.LJ.List[nome_peca]['Total']-=1
            self.popup(f'peça vendida por {self.tot_gl}', 'Congratulations!')
        self.d_Exit()

    def event_fiado(self):
        nm=self.Lista_de_pessoas.currentItem().text()
        self.CL.Clientes[nm]["Pendentes"][self.nome_gl]=self.tot_gl
        self.CL.Clientes[nm]["Total"]+=float(self.tot_gl.replace('R$', '').replace(',', '.'))
        self.d_Exit()

    def botao_pagar(self):
        pay=self.linePagar.text()
        if float(pay)<=0 and float(pay)<=self.CL.Clientes[self.nome_gl]["Total"]:
            self.linePagar.setPlaceholderText("Valor invalído!")
        else:
            self.CL.Clientes[self.nome_gl]["Total"]-=float(pay)
            self.d_Exit()

    def event_detalhes(self):
        self.nome_gl=self.listDevendo.currentItem().text()
        obj=self.CL.Clientes[self.nome_gl]
        self.Detalhe_cliente.show()

        self.P_Nome.setText(f'Nome: {self.nome_gl}')
        self.P_Telefone.setText(f'Telefone: {obj["Telefone"]}')
        self.P_Lugar.setText(f'Lugar: {obj["Cidade"]}')
        self.P_Total.setText(f'Total: {self.ConRS(obj["Total"])}')

        self.listPendentes.clear()
        for k in self.CL.Clientes[self.nome_gl]["Pendentes"].keys():
            self.listPendentes.addItem(f'{k}\t     {self.ConRS(self.LJ.List[k]["Preço"])}')

    def popup(self, msg, txt):
        pp=QMessageBox()
        pp.setWindowTitle(txt)
        pp.setText(msg)
        pp.exec_()

    def ConRS(self, RS):
        RS=f'{RS:.2f}'
        n=0
        Cnv=''
        for c in str(RS)[::-1]:
            if n==3:
                Cnv+=','
                n=0
            Cnv+=c
            n+=1

        return f"R${Cnv[::-1].replace(f',.', ',')}"

if __name__ == '__main__':
    qt = QApplication(argv)
    Janela = Main()
    Janela.show()
    qt.exec_()
