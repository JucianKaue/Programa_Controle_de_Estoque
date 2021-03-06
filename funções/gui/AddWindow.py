# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from funções import dados

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(dados.width(100), dados.heigth(100))
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setWindowIcon(QtGui.QIcon("C:/Users/jucia/PycharmProjects/Controle_de_Estoque/imagens/logo-quadrado.png"))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

# Imagem de Fundo - background
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, dados.width(100), dados.heigth(100)))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("C:/Users/jucia/PycharmProjects/Controle_de_Estoque/imagens/background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")

# Caixa de Mensagens - Labels
    # Def font title
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(36)

        # Title
        self.Label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.Label_titulo.setGeometry(QtCore.QRect(dados.width(30), dados.heigth(1), 600, 80))
        self.Label_titulo.setFont(font)
        self.Label_titulo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Label_titulo.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Label_titulo.setTextFormat(QtCore.Qt.PlainText)
        self.Label_titulo.setObjectName("Label_titulo")

    # Def font Labels
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        # Labels
        self.label_Codigo = QtWidgets.QLabel(self.centralwidget)
        self.label_Codigo.setGeometry(QtCore.QRect(dados.width(13), dados.heigth(12), 181, 51))
        self.label_Codigo.setFont(font)
        self.label_Codigo.setObjectName("label_Codigo")

        self.label_Tamanho = QtWidgets.QLabel(self.centralwidget)
        self.label_Tamanho.setGeometry(QtCore.QRect(dados.width(13), dados.heigth(20), 181, 51))
        self.label_Tamanho.setFont(font)
        self.label_Tamanho.setObjectName("label_Tamanho")

        self.Label_descricao = QtWidgets.QLabel(self.centralwidget)
        self.Label_descricao.setGeometry(QtCore.QRect(dados.width(13), dados.heigth(28), 171, 51))
        self.Label_descricao.setFont(font)
        self.Label_descricao.setObjectName("Label_descricao")

        self.Label_P_Entrada = QtWidgets.QLabel(self.centralwidget)
        self.Label_P_Entrada.setGeometry(QtCore.QRect(dados.width(13), dados.heigth(36), 251, 51))
        self.Label_P_Entrada.setFont(font)
        self.Label_P_Entrada.setObjectName("Label_P_Entrada")

        self.Label_P_Saida = QtWidgets.QLabel(self.centralwidget)
        self.Label_P_Saida.setGeometry(QtCore.QRect(dados.width(13), dados.heigth(44), 261, 51))
        self.Label_P_Saida.setFont(font)
        self.Label_P_Saida.setObjectName("Label_P_Sada")

        self.Label_Quant = QtWidgets.QLabel(self.centralwidget)
        self.Label_Quant.setGeometry(QtCore.QRect(dados.width(13), dados.heigth(52), 261, 51))
        self.Label_Quant.setFont(font)
        self.Label_Quant.setObjectName("Label_Quant")

        self.Label_data = QtWidgets.QLabel(self.centralwidget)
        self.Label_data.setGeometry(QtCore.QRect(dados.width(13), dados.heigth(60), 261, 51))
        self.Label_data.setFont(font)
        self.Label_data.setObjectName("Label_data")

# Text Boxes (input)
    # def Font Inputs
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(15)
        font.setWeight(75)

    # input boxes
        self.input_Cod = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Cod.setGeometry(QtCore.QRect(dados.width(36), dados.heigth(13), 350, 33))
        self.input_Cod.setObjectName("input_Cod")
        self.input_Cod.setFont(font)

        self.input_Tam = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Tam.setGeometry(QtCore.QRect(dados.width(36), dados.heigth(21), 350, 33))
        self.input_Tam.setObjectName("input_Tam")
        self.input_Tam.setFont(font)

        self.input_Desc = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Desc.setGeometry(QtCore.QRect(dados.width(36), dados.heigth(29), 350, 33))
        self.input_Desc.setObjectName("input_Desc")
        self.input_Desc.setFont(font)

        self.input_P_entrada = QtWidgets.QLineEdit(self.centralwidget)
        self.input_P_entrada.setGeometry(QtCore.QRect(dados.width(36), dados.heigth(37), 350, 33))
        self.input_P_entrada.setText('R$')
        self.input_P_entrada.setObjectName("input_P_entrada")
        self.input_P_entrada.setFont(font)

        self.input_P_Saida = QtWidgets.QLineEdit(self.centralwidget)
        self.input_P_Saida.setGeometry(QtCore.QRect(dados.width(36), dados.heigth(45), 350, 33))
        self.input_P_Saida.setText("R$")
        self.input_P_Saida.setObjectName("input_P_Saida")
        self.input_P_Saida.setFont(font)



        self.input_Quant = QtWidgets.QSpinBox(self.centralwidget)
        self.input_Quant.setGeometry(QtCore.QRect(dados.width(36), dados.heigth(53), 350, 33))
        self.input_Quant.setObjectName("spinBox")
        self.input_Quant.setValue(1)
        self.input_Quant.setFont(font)

# data
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(dados.width(36), dados.heigth(61), 350, 33))
        self.dateEdit.date()
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDate(QtCore.QDate(dados.data_hoje()))

# Botão Salvar
        self.PushButton_Save = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_Save.setGeometry(QtCore.QRect(dados.width(60), dados.heigth(73), 111, 41))
        self.PushButton_Save.setObjectName("PushButton_Save")
        self.PushButton_Save.clicked.connect(self.save)

# Botão Voltar
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(dados.width(20), dados.heigth(73), 75, 51))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/jucia/PycharmProjects/Controle_de_Estoque/imagens/Go-back-icon.png"), icon.Normal, icon.Off)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("Voltar")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# Main Window _ Janela Principal
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Controle de Estoque - Adicionar Produto"))
        self.Label_titulo.setText(_translate("MainWindow", "Adicionar Produtos"))
        self.label_Codigo.setText(_translate("MainWindow", "Código:"))
        self.Label_descricao.setText(_translate("MainWindow", "Descrição: "))
        self.label_Tamanho.setText(_translate("MainWindow", "Tamanho:"))
        self.Label_data.setText(_translate("MainWindow", "Data:"))
        self.Label_P_Saida.setText(_translate("MainWindow", "Preço de Saída:"))
        self.Label_P_Entrada.setText(_translate("MainWindow", "Preço de Entrada:"))
        self.Label_Quant.setText(_translate("MainWindow", "Quantidade: "))
        self.PushButton_Save.setText(_translate("MainWindow", "Salvar"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))

    def save(self):
        from funções.database import adicionar
        from funções import dados
        cod = self.input_Cod.text()
        tam = self.input_Tam.text()
        desc = self.input_Desc.text()
        preco_entrada = self.input_P_entrada.text()
        preco_saida = self.input_P_Saida.text()
        data = self.dateEdit.text()
        quantidade = self.input_Quant.text()
        preco_entrada = dados.dinheiro(preco_entrada)
        preco_saida = dados.dinheiro(preco_saida)
        data = dados.data(data)
        adicionar(
            codigo=cod,
            tamanho=tam,
            descricao=desc,
            preco_entrada=preco_entrada,
            preco_saida=preco_saida,
            dia_entrada=data,
            quantidade=quantidade
        )

'''
if __name__ == "__main__":
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())'''