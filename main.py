import sys

import connect
import enter
import grp_widget
import main_win
import reg
from PyQt5 import QtCore, QtGui, QtWidgets

#login window class
class win_enter(enter.Ui_Form, QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pb_reg.clicked.connect(self.show_reg_win)
		self.pb_enter.clicked.connect(self.login)

	def login(self):
		user = connect.get_user_by_login(self.le_login.text())
		if user["login"] == self.le_login.text() and user["pwd"] == self.le_password.text():
			self.master_win = win_main(user=user)
			self.master_win.show()
			self.close()

	def show_reg_win(self):
		self.reg_win = win_reg()
		self.reg_win.show()
		self.close()


#regestration window class
class win_reg(reg.Ui_Form, QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.back_to_enter)
		self.pb_next.clicked.connect(self.registration)

	def registration(self):
		print("check")
		if connect.check_login(self.le_login.text()) == True:
			msg = QtWidgets.QMessageBox()
			msg.setText("Такой логин уже занят")
			msg.exec_()
		elif self.le_pwd.text() != self.le_r_pwd.text():
			msg = QtWidgets.QMessageBox()
			msg.setText("Пароли не совпадают")
			msg.exec_()
		else:
			username=self.le_name.text()
			login=self.le_login.text()
			pwd=self.le_pwd.text()
			hobby=self.cb_hobby.currentIndex()
			about_me=self.pte_about.toPlainText()
			print(username)
			print(login)
			print(pwd)
			print(hobby)
			print(about_me)
			connect.post_new_user(
				username=username,
				login=login,
				pwd=pwd,
				hobby=hobby,
				about_me=about_me
			)


	def back_to_enter(self):
		self.enter_win = win_enter()
		self.enter_win.show()
		self.close()


#main_window_class
class win_main(main_win.Ui_Form, QtWidgets.QWidget):
	def __init__(self, user):
		self.user = user
		super().__init__()
		self.setupUi(self)

		self.pb_profile.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_profile))
		self.pb_anon.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_anon))
		self.pb_cons.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_cons))
		self.pb_groups.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_groups))
		self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_options))

		self.le_login.setPlaceholderText(user["login"])
		self.le_pwd.setPlaceholderText(user["pwd"])
		self.le_name.setPlaceholderText(user["username"])
		self.cb_hobby.setCurrentIndex(user["hobby"])
		self.pte_about.setPlaceholderText(user["ab_me"])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = win_enter()
    ui.show()
    sys.exit(app.exec_())