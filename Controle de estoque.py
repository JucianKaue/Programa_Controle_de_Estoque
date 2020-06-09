from Demos.win32gui_menu import MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtWidgets
import sys
from funções import database, dados
from funções.gui import Home, AddWindow


class MainWindow(Home.Ui_JanelaInicial):
    def __init__(self):
        super(MainWindow, self)


class Add_Window(AddWindow.Ui_MainWindow):
    def __init__(self):
        super(Add_Window, self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JanelaInicial = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(JanelaInicial)
    JanelaInicial.show()
    sys.exit(app.exec_())
