import sys
from gui import Ui_MainWindow
from PyQt5 import QtGui, QtCore, QtWidgets
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
last_name = config['settings']['last_name']


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.submit_button.clicked.connect(self.submit_func)
        self.ui.reset_button.clicked.connect(self.reset_func)
        self.ui.show_help_button.clicked.connect(self.show_help_func)
        self.ui.MainWindow.setWindowTitle(last_name)

    def submit_func(self):
        text = self.ui.lineEdit.text()
        config.set("settings", "last_name", text)
        with open("config.ini", 'w') as config_file:
            config.write(config_file)
        self.ui.MainWindow.setWindowTitle(text)

    def reset_func(self):
        self.ui.MainWindow.setWindowTitle('Discord custom game activity')
        self.ui.lineEdit.setText('')

    def show_help_func(self):
        # messageBox = QtWidgets.QMessageBox()
        # ok = messageBox.question(
        #     self, f"How to use.\nEnter custom game name in the text area and click Submit\nThen change game activity in discord to the selected name.\nThat's all!")
        # if ok == QtWidgets.QMessageBox.Yes:
        #     pass
        messageBox = QtWidgets.QMessageBox()
        ok = messageBox.question(
            self, f'Delete')
        if ok == QtWidgets.QMessageBox.Yes:
            pass


app = QtWidgets.QApplication(sys.argv)
application = Main()
application.show()

sys.exit(app.exec())
