from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from GUI import *
from sys import argv
from loja import *

class Main(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.LJ=Loja()

        # Funções 1
        self.d_Exit()
        self.LJ.carregar()
        # Funções 2
        self.R_pecas.clicked.connect(self.PR_pecas.show)
        self.BTT_peca.clicked.connect(self.d_registrar_pecas)
        self.Exit.clicked.connect(self.d_Exit)
        self.L_pecas.clicked.connect(self.L2_pecas)
        self.actionSalvar.triggered.connect(self.LJ.salvar)
        
    def d_registrar_pecas(self): # Terminar prenchimento de daods da peça
        msg='Este campo é obrigatorio!'
        prenchido=False

        v_pr=self.Preco.text().replace(' ', '')
        if v_pr=='':
            self.Preco.setPlaceholderText(msg)
            prenchido=True
            
        v_pe=self.Pecas.text().replace(' ', '')
        if v_pe=='':
            self.Pecas.setPlaceholderText(msg)
            prenchido=True

        v_mo=self.Mao_O.text().replace(' ', '')
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

    def update_list_pecas(self):
        self.listPecas.clear()

        for p in self.LJ.List:
            self.listPecas.addItem(f'{p["Peça"]}\t\t\t\t{self.ConRS(p["Preço"])}')

    def d_Exit(self):
        self.PR_pecas.close()
        self.PR_pecas.close()
        self.PL_pecas.close()

    def L2_pecas(self):
        self.PL_pecas.show() 
        self.update_list_pecas()

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