# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enter.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(441, 587)
        Form.setStyleSheet("#Form{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.869, y2:0.403818, stop:0 rgba(46, 183, 169, 255), stop:1 rgba(255, 146, 255, 255));\n"
"}\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(352, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 485, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 43, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        self.frame_main = QtWidgets.QFrame(Form)
        self.frame_main.setStyleSheet("#frame_main{\n"
"    border-radius: 12;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_main)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        spacerItem4 = QtWidgets.QSpacerItem(20, 85, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_main)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_main)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.le_username = QtWidgets.QLineEdit(self.frame_main)
        self.le_username.setStyleSheet("border-radius: 5;\n"
"border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0.869, y2:0.403818, stop:0 rgba(46, 183, 169, 255), stop:1 rgba(255, 146, 255, 255));\n"
"padding: 2;")
        self.le_username.setObjectName("le_username")
        self.gridLayout_2.addWidget(self.le_username, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_main)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.le_password = QtWidgets.QLineEdit(self.frame_main)
        self.le_password.setStyleSheet("border-radius: 5;\n"
"border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0.869, y2:0.403818, stop:0 rgba(46, 183, 169, 255), stop:1 rgba(255, 146, 255, 255));\n"
"padding: 2;")
        self.le_password.setObjectName("le_password")
        self.gridLayout_2.addWidget(self.le_password, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.pb_enter = QtWidgets.QPushButton(self.frame_main)
        self.pb_enter.setStyleSheet("QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.869, y2:0.403818, stop:0 rgba(46, 183, 169, 255), stop:1 rgba(255, 146, 255, 255));\n"
"border: none;\n"
"border-radius: 10;\n"
"padding: 7;\n"
"}\n"
"QPushButton:hover:pressed{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 16, 225, 255), stop:1 rgba(255, 72, 255, 255));\n"
"    color:  white;\n"
"}")
        self.pb_enter.setObjectName("pb_enter")
        self.verticalLayout.addWidget(self.pb_enter)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 85, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_main)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.pb_reg = QtWidgets.QPushButton(self.frame_main)
        self.pb_reg.setFlat(True)
        self.pb_reg.setObjectName("pb_reg")
        self.verticalLayout_2.addWidget(self.pb_reg, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout.addWidget(self.frame_main, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 10)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 10)
        self.gridLayout.setRowStretch(2, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "ВХОД"))
        self.pushButton.setText(_translate("Form", "Забыли пароль?"))
        self.label_2.setText(_translate("Form", "Логин:"))
        self.label_3.setText(_translate("Form", "Пароль:"))
        self.pb_enter.setText(_translate("Form", "Войти"))
        self.label_4.setText(_translate("Form", "нет аккаунта?"))
        self.pb_reg.setText(_translate("Form", "РЕГЕСТРАЦИЯ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
