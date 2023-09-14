# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\uis\main_win.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(752, 523)
        Form.setStyleSheet("QLabel{\n"
"    \n"
"    font: 10pt \"Gadugi\";\n"
"}\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_menu = QtWidgets.QFrame(Form)
        self.frame_menu.setStyleSheet("#frame_menu{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.869, y2:0.403818, stop:0 rgba(46, 183, 169, 255), stop:1 rgba(255, 146, 255, 255));\n"
"}")
        self.frame_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setLineWidth(0)
        self.frame_menu.setObjectName("frame_menu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_menu)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.frame_menu)
        self.frame.setStyleSheet("border: None;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(".\\uis\\../icons/main_ico.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("font: 11pt \"Gadugi\";")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.frame_btns = QtWidgets.QFrame(self.frame_menu)
        self.frame_btns.setStyleSheet("QPushButton{\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.869, y2:0.403818, stop:0 rgba(46, 183, 169, 255), stop:1 rgba(255, 146, 255, 255));\n"
"background-color:rgb(81, 81, 81);\n"
"border-radius: 10;\n"
"padding: 7;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(14, 0, 255, 255), stop:1 rgba(0, 255, 104, 255));\n"
"background-color:rgb(227, 227, 227);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"color:rgb(227, 227, 227) ;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(14, 0, 255, 255), stop:1 rgba(0, 255, 104, 255));\n"
"\n"
"}\n"
"\n"
"#frame_btns{\n"
"    padding-left: 30;\n"
"    padding-right: 30;\n"
"    border: None;\n"
"}")
        self.frame_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_btns.setObjectName("frame_btns")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_btns)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pb_profile = QtWidgets.QPushButton(self.frame_btns)
        self.pb_profile.setStyleSheet("")
        self.pb_profile.setFlat(False)
        self.pb_profile.setObjectName("pb_profile")
        self.verticalLayout_2.addWidget(self.pb_profile)
        self.pb_groups = QtWidgets.QPushButton(self.frame_btns)
        self.pb_groups.setObjectName("pb_groups")
        self.verticalLayout_2.addWidget(self.pb_groups)
        self.pb_anon = QtWidgets.QPushButton(self.frame_btns)
        self.pb_anon.setObjectName("pb_anon")
        self.verticalLayout_2.addWidget(self.pb_anon)
        self.pb_cons = QtWidgets.QPushButton(self.frame_btns)
        self.pb_cons.setObjectName("pb_cons")
        self.verticalLayout_2.addWidget(self.pb_cons)
        self.pushButton = QtWidgets.QPushButton(self.frame_btns)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame_btns, 0, QtCore.Qt.AlignVCenter)
        self.frame_3 = QtWidgets.QFrame(self.frame_menu)
        self.frame_3.setStyleSheet("border: None;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame_menu)
        self.frame_content = QtWidgets.QFrame(Form)
        self.frame_content.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.frame_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_content)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_content)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pg_hello = QtWidgets.QWidget()
        self.pg_hello.setObjectName("pg_hello")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.pg_hello)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.pg_hello)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.stackedWidget.addWidget(self.pg_hello)
        self.pg_profile = QtWidgets.QWidget()
        self.pg_profile.setObjectName("pg_profile")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.pg_profile)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_top_profile = QtWidgets.QFrame(self.pg_profile)
        self.frame_top_profile.setStyleSheet("\n"
"background-color: rgb(81, 81, 81);\n"
"\n"
"")
        self.frame_top_profile.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top_profile.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_profile.setObjectName("frame_top_profile")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_top_profile)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.frame_top_profile)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Sans Serif\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_9.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addWidget(self.frame_top_profile)
        self.frame_4 = QtWidgets.QFrame(self.pg_profile)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_11 = QtWidgets.QLabel(self.frame_6)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_17.addWidget(self.label_11)
        self.label_17 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_17.addWidget(self.label_17)
        self.le_name = QtWidgets.QLineEdit(self.frame_6)
        self.le_name.setStyleSheet("border-radius: 5;\n"
"border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0.869, y2:0.403818, stop:0 rgba(46, 183, 169, 255), stop:1 rgba(255, 146, 255, 255));\n"
"padding: 2;")
        self.le_name.setObjectName("le_name")
        self.verticalLayout_17.addWidget(self.le_name)
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_17.addWidget(self.label_13)
        self.le_pwd = QtWidgets.QLineEdit(self.frame_6)
        self.le_pwd.setStyleSheet("border-radius: 5;\n"
"border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0.869, y2:0.403818, stop:0 rgba(46, 183, 169, 255), stop:1 rgba(255, 146, 255, 255));\n"
"padding: 2;")
        self.le_pwd.setObjectName("le_pwd")
        self.verticalLayout_17.addWidget(self.le_pwd)
        self.label_15 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_17.addWidget(self.label_15)
        self.le_r_pwd = QtWidgets.QLineEdit(self.frame_6)
        self.le_r_pwd.setStyleSheet("border-radius: 5;\n"
"border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0.869, y2:0.403818, stop:0 rgba(46, 183, 169, 255), stop:1 rgba(255, 146, 255, 255));\n"
"padding: 2;")
        self.le_r_pwd.setObjectName("le_r_pwd")
        self.verticalLayout_17.addWidget(self.le_r_pwd)
        self.label_14 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_17.addWidget(self.label_14)
        self.cb_hobby = QtWidgets.QComboBox(self.frame_6)
        self.cb_hobby.setStyleSheet("QComboBox{\n"
"border-radius: 5;\n"
"border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0.869, y2:0.403818, stop:0 rgba(46, 183, 169, 255), stop:1 rgba(255, 146, 255, 255));\n"
"padding: 2;\n"
"}\n"
"QComboBox::drop-down { \n"
"height: 0px;                    \n"
"width: 0px;\n"
"                    \n"
"                     }")
        self.cb_hobby.setIconSize(QtCore.QSize(16, 16))
        self.cb_hobby.setFrame(True)
        self.cb_hobby.setObjectName("cb_hobby")
        self.cb_hobby.addItem("")
        self.cb_hobby.addItem("")
        self.cb_hobby.addItem("")
        self.cb_hobby.addItem("")
        self.cb_hobby.addItem("")
        self.cb_hobby.addItem("")
        self.cb_hobby.addItem("")
        self.cb_hobby.addItem("")
        self.cb_hobby.addItem("")
        self.cb_hobby.addItem("")
        self.verticalLayout_17.addWidget(self.cb_hobby)
        self.label_16 = QtWidgets.QLabel(self.frame_6)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_17.addWidget(self.label_16)
        self.pte_about = QtWidgets.QPlainTextEdit(self.frame_6)
        self.pte_about.setStyleSheet("border-radius: 5;\n"
"border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0.869, y2:0.403818, stop:0 rgba(46, 183, 169, 255), stop:1 rgba(255, 146, 255, 255));\n"
"padding: 2;")
        self.pte_about.setObjectName("pte_about")
        self.verticalLayout_17.addWidget(self.pte_about)
        self.verticalLayout_18.addLayout(self.verticalLayout_17)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.869, y2:0.403818, stop:0 rgba(46, 183, 169, 255), stop:1 rgba(255, 146, 255, 255));\n"
"background-color:rgb(81, 81, 81);\n"
"border-radius: 10;\n"
"padding: 7;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(14, 0, 255, 255), stop:1 rgba(0, 255, 104, 255));\n"
"background-color:rgb(227, 227, 227);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"color:rgb(227, 227, 227) ;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(14, 0, 255, 255), stop:1 rgba(0, 255, 104, 255));\n"
"\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_18.addWidget(self.pushButton_2)
        self.horizontalLayout_4.addWidget(self.frame_6)
        self.horizontalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 12)
        self.stackedWidget.addWidget(self.pg_profile)
        self.pg_groups = QtWidgets.QWidget()
        self.pg_groups.setObjectName("pg_groups")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pg_groups)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.pg_groups)
        self.frame_5.setStyleSheet("\n"
"background-color: rgb(81, 81, 81);\n"
"\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Sans Serif\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_12.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.frame_top_groups = QtWidgets.QFrame(self.pg_groups)
        self.frame_top_groups.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top_groups.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_groups.setObjectName("frame_top_groups")
        self.layout_groups = QtWidgets.QVBoxLayout(self.frame_top_groups)
        self.layout_groups.setObjectName("layout_groups")
        self.verticalLayout_5.addWidget(self.frame_top_groups)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 12)
        self.stackedWidget.addWidget(self.pg_groups)
        self.pg_anon = QtWidgets.QWidget()
        self.pg_anon.setObjectName("pg_anon")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.pg_anon)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_7 = QtWidgets.QFrame(self.pg_anon)
        self.frame_7.setStyleSheet("\n"
"background-color: rgb(81, 81, 81);\n"
"\n"
"")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Sans Serif\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_13.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_6.addWidget(self.frame_7)
        self.frame_top_anon = QtWidgets.QFrame(self.pg_anon)
        self.frame_top_anon.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top_anon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_anon.setObjectName("frame_top_anon")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_top_anon)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_9 = QtWidgets.QLabel(self.frame_top_anon)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_14.addWidget(self.label_9)
        self.verticalLayout_6.addWidget(self.frame_top_anon)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 12)
        self.stackedWidget.addWidget(self.pg_anon)
        self.pg_cons = QtWidgets.QWidget()
        self.pg_cons.setObjectName("pg_cons")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.pg_cons)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_top_cons = QtWidgets.QFrame(self.pg_cons)
        self.frame_top_cons.setStyleSheet("\n"
"background-color: rgb(81, 81, 81);\n"
"\n"
"")
        self.frame_top_cons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top_cons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_cons.setObjectName("frame_top_cons")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_top_cons)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.frame_top_cons)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Sans Serif\";")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_11.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addWidget(self.frame_top_cons)
        self.frame_10 = QtWidgets.QFrame(self.pg_cons)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_10 = QtWidgets.QLabel(self.frame_10)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_15.addWidget(self.label_10)
        self.verticalLayout_7.addWidget(self.frame_10)
        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 12)
        self.stackedWidget.addWidget(self.pg_cons)
        self.pg_options = QtWidgets.QWidget()
        self.pg_options.setObjectName("pg_options")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.pg_options)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_top_opt = QtWidgets.QFrame(self.pg_options)
        self.frame_top_opt.setStyleSheet("\n"
"background-color: rgb(81, 81, 81);\n"
"\n"
"")
        self.frame_top_opt.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top_opt.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_opt.setObjectName("frame_top_opt")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_top_opt)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.frame_top_opt)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Sans Serif\";")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.verticalLayout_8.addWidget(self.frame_top_opt)
        self.frame_12 = QtWidgets.QFrame(self.pg_options)
        font = QtGui.QFont()
        font.setFamily("Futura Bk BT")
        font.setPointSize(10)
        self.frame_12.setFont(font)
        self.frame_12.setStyleSheet("Qlabel{\n"
"    font: 24pt \"Gadugi\";\n"
"}")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_2 = QtWidgets.QFrame(self.frame_12)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setStyleSheet("QComboBox{\n"
"border-radius: 5;\n"
"border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0.869, y2:0.403818, stop:0 rgba(46, 183, 169, 255), stop:1 rgba(255, 146, 255, 255));\n"
"padding: 2;\n"
"}\n"
"QComboBox::drop-down { \n"
"height: 0px;                    \n"
"width: 0px;\n"
"                    \n"
"                     }")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox)
        self.verticalLayout_16.addWidget(self.frame_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem)
        self.verticalLayout_8.addWidget(self.frame_12)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 12)
        self.stackedWidget.addWidget(self.pg_options)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.frame_content)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "СОЦИАЛЬНЫЙ КОМПАНЬОН"))
        self.pb_profile.setText(_translate("Form", "Профиль"))
        self.pb_groups.setText(_translate("Form", "Группы"))
        self.pb_anon.setText(_translate("Form", "Анонимные чаты"))
        self.pb_cons.setText(_translate("Form", "Проф. консультации"))
        self.pushButton.setText(_translate("Form", "Настройки"))
        self.label_3.setText(_translate("Form", "Добро пожаловать!\n"
"Вас приветствует приложение Социальный Компаньон.\n"
" С помощью этого приложения вы сможете:\n"
"1.Найти новых друзей со схожими интересами.\n"
"2.Попереписываться с людьми, у которых похожие проблемы.\n"
"3.Записаться на консультацию профессионального психолога.\n"
"4. Или, если Вы хотите оставить вашу личность в тайне, у нас есть Анонимный чат!"))
        self.label_4.setText(_translate("Form", "ПРОФИЛЬ"))
        self.label_11.setText(_translate("Form", "Редактирование профиля {profile_login}:"))
        self.label_17.setText(_translate("Form", "Имя:"))
        self.label_13.setText(_translate("Form", "Пароль:"))
        self.label_15.setText(_translate("Form", "Повторите пароль:"))
        self.label_14.setText(_translate("Form", "Ваше основное хобби:"))
        self.cb_hobby.setItemText(0, _translate("Form", "Не выбрано"))
        self.cb_hobby.setItemText(1, _translate("Form", "Путешествия"))
        self.cb_hobby.setItemText(2, _translate("Form", "Спорт"))
        self.cb_hobby.setItemText(3, _translate("Form", "Исскуство"))
        self.cb_hobby.setItemText(4, _translate("Form", "Пение"))
        self.cb_hobby.setItemText(5, _translate("Form", "Танцы"))
        self.cb_hobby.setItemText(6, _translate("Form", "Настольные игры"))
        self.cb_hobby.setItemText(7, _translate("Form", "Компьютерные игры"))
        self.cb_hobby.setItemText(8, _translate("Form", "Чтение"))
        self.cb_hobby.setItemText(9, _translate("Form", "Другое"))
        self.label_16.setText(_translate("Form", "О себе:"))
        self.pushButton_2.setText(_translate("Form", "Подтвердить изменения"))
        self.label_5.setText(_translate("Form", "ГРУППЫ"))
        self.label_6.setText(_translate("Form", "АНОНИМНЫЕ ЧАТЫ"))
        self.label_9.setText(_translate("Form", "В Разработке"))
        self.label_7.setText(_translate("Form", "КОНСУЛЬТАЦИИ СО СПЕЦИАЛИСТОМ"))
        self.label_10.setText(_translate("Form", "В Разработке"))
        self.label_8.setText(_translate("Form", "НАСТРОЙКИ"))
        self.label_12.setText(_translate("Form", "Страница по умолчанию при открытии приложения:"))
        self.comboBox.setItemText(0, _translate("Form", "Приветственное сообщение"))
        self.comboBox.setItemText(1, _translate("Form", "Профиль"))
        self.comboBox.setItemText(2, _translate("Form", "Группы"))
        self.comboBox.setItemText(3, _translate("Form", "Анонимные чаты"))
        self.comboBox.setItemText(4, _translate("Form", "Проф. Консультации"))
        self.comboBox.setItemText(5, _translate("Form", "Настройки"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
