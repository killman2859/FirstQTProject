# Form implementation generated from reading ui file 'Forms/RegistrationFormDesign.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_RegistrationForm(object):
    def setupUi(self, RegistrationForm):
        RegistrationForm.setObjectName("RegistrationForm")
        RegistrationForm.resize(270, 360)
        RegistrationForm.setMinimumSize(QtCore.QSize(270, 360))
        RegistrationForm.setMaximumSize(QtCore.QSize(270, 360))
        self.centralwidget = QtWidgets.QWidget(parent=RegistrationForm)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 0, 175, 301))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.nameTextBox = QtWidgets.QLineEdit(parent=self.widget)
        self.nameTextBox.setObjectName("nameTextBox")
        self.verticalLayout.addWidget(self.nameTextBox)
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.surnameTextBox = QtWidgets.QLineEdit(parent=self.widget)
        self.surnameTextBox.setObjectName("surnameTextBox")
        self.verticalLayout.addWidget(self.surnameTextBox)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.loginTextBox = QtWidgets.QLineEdit(parent=self.widget)
        self.loginTextBox.setObjectName("loginTextBox")
        self.verticalLayout.addWidget(self.loginTextBox)
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.passwordTextBox = QtWidgets.QLineEdit(parent=self.widget)
        self.passwordTextBox.setObjectName("passwordTextBox")
        self.verticalLayout.addWidget(self.passwordTextBox)
        self.registerButton = QtWidgets.QPushButton(parent=self.widget)
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout.addWidget(self.registerButton)
        RegistrationForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=RegistrationForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 270, 26))
        self.menubar.setObjectName("menubar")
        RegistrationForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=RegistrationForm)
        self.statusbar.setObjectName("statusbar")
        RegistrationForm.setStatusBar(self.statusbar)

        self.retranslateUi(RegistrationForm)
        QtCore.QMetaObject.connectSlotsByName(RegistrationForm)

    def retranslateUi(self, RegistrationForm):
        _translate = QtCore.QCoreApplication.translate
        RegistrationForm.setWindowTitle(_translate("RegistrationForm", "Registation"))
        self.label.setText(_translate("RegistrationForm", "Регистрация"))
        self.label_4.setText(_translate("RegistrationForm", "Имя"))
        self.label_5.setText(_translate("RegistrationForm", "Фамилия"))
        self.label_2.setText(_translate("RegistrationForm", "Логин"))
        self.label_3.setText(_translate("RegistrationForm", "Пароль"))
        self.registerButton.setText(_translate("RegistrationForm", "Зарегистрироваться"))
