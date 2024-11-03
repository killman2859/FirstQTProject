

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AuthorizationForm(object):
    def setupUi(self, AuthorizationForm):
        AuthorizationForm.setObjectName("AuthorizationForm")
        AuthorizationForm.resize(244, 279)
        AuthorizationForm.setMinimumSize(QtCore.QSize(244, 279))
        AuthorizationForm.setMaximumSize(QtCore.QSize(244, 279))
        self.centralwidget = QtWidgets.QWidget(parent=AuthorizationForm)
        self.centralwidget.setObjectName("centralwidget")
        self.registerButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(100, 200, 141, 21))
        self.registerButton.setStyleSheet("color:rgb(0,0,255)")
        self.registerButton.setCheckable(False)
        self.registerButton.setAutoDefault(False)
        self.registerButton.setDefault(False)
        self.registerButton.setFlat(True)
        self.registerButton.setObjectName("registerButton")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 10, 182, 189))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
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
        self.authButton = QtWidgets.QPushButton(parent=self.widget)
        self.authButton.setObjectName("authButton")
        self.verticalLayout.addWidget(self.authButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        AuthorizationForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=AuthorizationForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 244, 26))
        self.menubar.setObjectName("menubar")
        AuthorizationForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=AuthorizationForm)
        self.statusbar.setObjectName("statusbar")
        AuthorizationForm.setStatusBar(self.statusbar)

        self.retranslateUi(AuthorizationForm)
        QtCore.QMetaObject.connectSlotsByName(AuthorizationForm)

    def retranslateUi(self, AuthorizationForm):
        _translate = QtCore.QCoreApplication.translate
        AuthorizationForm.setWindowTitle(_translate("AuthorizationForm", "Authorization"))
        self.registerButton.setText(_translate("AuthorizationForm", "У меня нет аккаунта"))
        self.label_2.setText(_translate("AuthorizationForm", "Авторизация"))
        self.label.setText(_translate("AuthorizationForm", "Логин"))
        self.label_3.setText(_translate("AuthorizationForm", "Пароль"))
        self.authButton.setText(_translate("AuthorizationForm", "Авторизоваться"))