# Form implementation generated from reading ui file '.\uis\grp_widget.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(501, 66)
        Form.setStyleSheet("#Form{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(14, 0, 255, 255), stop:1 rgba(0, 255, 104, 255));\n"
"}\n"
"QLabel{\n"
"font: 63 12pt \"Segoe UI Semibold\";\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_name = QtWidgets.QLabel(parent=Form)
        self.lbl_name.setObjectName("lbl_name")
        self.verticalLayout.addWidget(self.lbl_name)
        self.lbl_desc = QtWidgets.QLabel(parent=Form)
        self.lbl_desc.setObjectName("lbl_desc")
        self.verticalLayout.addWidget(self.lbl_desc)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_name.setText(_translate("Form", "Название"))
        self.lbl_desc.setText(_translate("Form", "Описание"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
