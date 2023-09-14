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
		check = connect.check_login(self.le_login.text())
		if check == False:
			msg = QtWidgets.QMessageBox()
			msg.setText("логин или пароль были введены неправильно, проверьте валидность введных данных и повторите попытку")
			msg.exec_()

		else:
			user = connect.get_user_by_login(self.le_login.text())
			if user["login"] == self.le_login.text() and user["pwd"] == self.le_password.text():
				self.master_win = win_main(user=user)
				self.master_win.show()
				self.close()
			else:
				msg = QtWidgets.QMessageBox()
				msg.setText("логин или пароль были введены неправильно, проверьте валидность введных данных и повторите попытку")
				msg.exec_()
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
			username = self.le_name.text()
			login    = self.le_login.text()
			pwd      = self.le_pwd.text()
			hobby    = self.cb_hobby.currentIndex()
			about_me = self.pte_about.toPlainText()

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

			msg = QtWidgets.QMessageBox()
			msg.setText("Учетная запись успешно создана, теперь вы можете войти")
			msg.exec_()

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
		with open("data/entered.txt", "r") as f:
			self.stackedWidget.setCurrentIndex(int(f.read()))

		self.pb_profile.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_profile))
		self.pb_anon.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_anon))
		self.pb_cons.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_cons))
		self.pb_groups.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_groups))
		self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_options))

		self.label_11.setText(f"Редактирование профиля {user['login']}:")
		self.le_name.setText(user["username"])
		self.cb_hobby.setCurrentIndex(user["hobby"])
		self.pte_about.setPlainText(user["ab_me"])

		self.pushButton_2.clicked.connect(self.edit_profile)
		self.comboBox.currentIndexChanged.connect(self.show_hello_page)


	def edit_profile(self):
		if self.le_pwd.text() != self.le_r_pwd.text():
			msg = QtWidgets.QMessageBox()
			msg.setText("Пароли не совпадают")
			msg.exec_()
			return
		else:
			self.user["username"] = self.le_name.text() if self.le_name.text() != self.user["username"] else self.user["username"]
			self.user["pwd"] = self.le_pwd.text() if self.le_pwd.text() != self.user["pwd"] else self.user["pwd"]
			self.user["hobby"] = self.cb_hobby.currentIndex() if self.cb_hobby.currentIndex() != self.user["hobby"] else self.user["hobby"]
			self.user["ab_me"] = self.pte_about.toPlainText() if self.pte_about.toPlainText() != self.user["ab_me"] else self.user["ab_me"]

			connect.edit_user_by_login(
				login=self.user["login"],
				username=self.user["username"],
				pwd=self.user["pwd"],
				hobby=self.user["hobby"],
				about_me=self.user["ab_me"]
			)

	def show_hello_page(self):
		with open("data/entered.txt", "w") as f:
			f.write(str(self.comboBox.currentIndex()))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = win_enter()
    ui.show()
    sys.exit(app.exec_())