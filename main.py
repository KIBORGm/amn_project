import sys

import enter
from PyQt5 import QtCore, QtGui, QtWidgets


class win_enter(enter.Ui_Form, QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pb_reg.clicked.connect(self.show_reg_win)

	def show_reg_win(self):
		#temp
		msg = QtWidgets.QMessageBox()
		msg.setText("у никиты разъебано очко")
		msg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = win_enter()
    ui.show()
    sys.exit(app.exec_())