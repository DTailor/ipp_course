import sys
from PyQt4 import QtGui, QtCore
from app_gui import App_Gui


class App(QtGui.QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.ui = App_Gui()
        self.ui.setup(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = App()
    myapp.show()
    sys.exit(app.exec_())
