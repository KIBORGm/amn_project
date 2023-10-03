import sys

import connect
import enter
import grp_widget
import main_win
import reg
from PyQt6 import QtCore, QtGui, QtWidgets

def show_base_msg(text, title="Социальный компаньон"):
	msg = QtWidgets.QMessageBox()
	msg.setText(text)
	msg.setWindowTitle(title)
	msg.exec()


#login window class
class win_enter(enter.Ui_Form, QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pb_reg.clicked.connect(self.show_reg_win)
		self.pb_enter.clicked.connect(self.login)

	def login(self):
		if connect.is_connected() == False:
			show_base_msg("Нет соединения с сервером. Проверьте подключение и повторите попытку")
			return
		if len(self.le_login.text()) != 0 and len(self.le_password.text()) != 0:
			check = connect.get_data(f"/users/{self.le_login.text()}")

			if check == None:
				show_base_msg("логин или пароль были введены неправильно, проверьте валидность введных данных и повторите попытку")

			else:
				user = connect.get_data(f"/users/{self.le_login.text()}")
				user["login"] = self.le_login.text()
				if user["pwd"] == self.le_password.text():
					self.master_win = win_main(user=user)
					self.master_win.show()
					self.close()
				else:
					show_base_msg(
						text="логин или пароль были введены неправильно, проверьте валидность введных данных и повторите попытку")
		else:
			show_base_msg(text="Пожалуйста введите логин и пароль")

	def show_reg_win(self):
		self.reg_win = win_reg()
		self.reg_win.show()
		self.close()


#regestration window class
class win_reg(reg.Ui_Form, QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pb_back_to_enter.clicked.connect(self.back_to_enter)
		self.pb_next.clicked.connect(self.registration)

	def registration(self):

		if connect.get_data(f"/users/{self.le_login.text()}") != None:
			show_base_msg(text="Такой логин уже занят. Попробуйте другой")
		elif self.le_pwd.text() != self.le_r_pwd.text():
			show_base_msg(text="Введенные пароли не совпадают.")
		elif len(self.le_pwd.text()) < 8:
			show_base_msg(text="Пароль слишком короткий, пожалуйста придумайте более сложный пароль.")
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
			connect.patch_data(
				url_data=f"/users/{login}",
				username=username,
				pwd=pwd,
				hobby=hobby,
				ab_me=about_me
			)

			show_base_msg(text="Учетная запись успешно создана, теперь вы можете войти")

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
		self.pb_options.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_options))

		self.label_11.setText(f"Редактирование профиля \"{user['login']}\":")
		self.le_name.setText(user["username"])
		self.cb_hobby.setCurrentIndex(user["hobby"])
		self.pte_about.setPlainText(user["ab_me"])

		self.pb_changes_submit.clicked.connect(self.edit_profile)
		self.cb_hobby.currentIndexChanged.connect(self.show_hello_page)

	def edit_profile(self):
		if len(self.le_pwd.text()) < 8:
			show_base_msg(text="Пароль слишком короткий, пожалуйста придумайте более сложный пароль.")
		elif self.le_pwd.text() != self.le_r_pwd.text():
			show_base_msg(text="Пароли не совпадают")
			return
		else:
			self.user["username"] = self.le_name.text() if self.le_name.text() != self.user["username"] else self.user["username"]
			self.user["pwd"] = self.le_pwd.text() if self.le_pwd.text() != self.user["pwd"] else self.user["pwd"]
			self.user["hobby"] = self.cb_hobby.currentIndex() if self.cb_hobby.currentIndex() != self.user["hobby"] else self.user["hobby"]
			self.user["ab_me"] = self.pte_about.toPlainText() if self.pte_about.toPlainText() != self.user["ab_me"] else self.user["ab_me"]

			connect.patch_data(
				url_data=f'/users/{self.user["login"]}/',
				username=self.user["username"],
				pwd=self.user["pwd"],
				hobby=self.user["hobby"],
				ab_me=self.user["ab_me"]
			)
			show_base_msg(text="Изменения были успешно внесены")

	def show_hello_page(self):
		with open("data/entered.txt", "w") as f:
			f.write(str(self.cb_hobby.currentIndex()))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = win_enter()
    ui.show()
    sys.exit(app.exec())