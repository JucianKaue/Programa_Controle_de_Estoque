# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Janela_Principal_grid.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JanelaInicial(object):
    def setupUi(self, JanelaInicial):
        JanelaInicial.setObjectName("JanelaInicial")
        JanelaInicial.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/users/jucia/PycharmProjects/Controle_de_Estoque/imagens/logo-quadrado.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        JanelaInicial.setWindowIcon(icon)
        JanelaInicial.setLayoutDirection(QtCore.Qt.LeftToRight)
        JanelaInicial.setStyleSheet("background-color: \'#bfbfbf\'")
        JanelaInicial.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        JanelaInicial.setDocumentMode(False)

        self.centralwidget = QtWidgets.QWidget(JanelaInicial)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        font = QtGui.QFont()
        font.setFamily("Noto Serif Cond")
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)

        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setEnabled(True)
        self.titulo.setFont(font)
        self.titulo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.titulo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.titulo.setTextFormat(QtCore.Qt.AutoText)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setWordWrap(False)
        self.titulo.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.titulo.setObjectName("titulo")
        self.gridLayout.addWidget(self.titulo, 0, 0, 1, 1)

        font.setPointSize(28)

        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setBaseSize(QtCore.QSize(80, 0))
        self.pushButton_add.setFont(font)
        self.pushButton_add.setMinimumSize(600, 65)
        self.pushButton_add.setStyleSheet("background-color: \'#82ff64\'")
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 2, 0, 1, 1)

        self.pushButton_view = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_view.setFont(font)
        self.pushButton_view.setMaximumSize(600, 65)
        self.pushButton_view.setStyleSheet("background-color: \'#07d1fb\'")
        self.pushButton_view.setObjectName("pushButton_view")
        self.gridLayout.addWidget(self.pushButton_view, 3, 0, 1, 1)

        self.pushButton_sell = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sell.setFont(font)
        self.pushButton_sell.setMaximumSize(600, 65)
        self.pushButton_sell.setStyleSheet("background-color: \'#ff4d4d\'")
        self.pushButton_sell.setObjectName("pushButton_sell")
        self.gridLayout.addWidget(self.pushButton_sell, 4, 0, 1, 1)

        JanelaInicial.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JanelaInicial)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 836, 21))
        self.menubar.setObjectName("menubar")
        JanelaInicial.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(JanelaInicial)
        self.statusbar.setObjectName("statusbar")
        JanelaInicial.setStatusBar(self.statusbar)

        self.retranslateUi(JanelaInicial)
        QtCore.QMetaObject.connectSlotsByName(JanelaInicial)

    def retranslateUi(self, JanelaInicial):
        _translate = QtCore.QCoreApplication.translate
        JanelaInicial.setWindowTitle(_translate("JanelaInicial", "Painel Principal"))
        self.pushButton_view.setText(_translate("JanelaInicial", "Estoque"))
        self.pushButton_add.setText(_translate("JanelaInicial", "Adiconar Produtos"))
        self.titulo.setText(_translate("JanelaInicial", "Controle de Estoque"))
        self.pushButton_sell.setText(_translate("JanelaInicial", "Dar baixa"))

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JanelaInicial = QtWidgets.QMainWindow()
    ui = Ui_JanelaInicial()
    ui.setupUi(JanelaInicial)
    JanelaInicial.show()
    sys.exit(app.exec_())
'''