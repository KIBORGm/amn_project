import sys

import enter
import grp_widget
import main_win
import reg
from PyQt5 import QtCore, QtGui, QtWidgets


class win_enter(enter.Ui_Form, QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pb_reg.clicked.connect(self.show_reg_win)

	def show_reg_win(self):
		self.reg_win = win_reg()
		self.reg_win.show()
		self.close()


class win_reg(reg.Ui_Form, QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.back_to_enter)

	def back_to_enter(self):
		self.enter_win = win_enter()
		self.enter_win.show()
		self.close()


class win_main(main_win.Ui_Form, QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi(self)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = win_enter()
    ui.show()
    sys.exit(app.exec_())