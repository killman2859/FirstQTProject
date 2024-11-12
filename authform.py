import sys

from PyQt6.QtPrintSupport import QPrintDialog

from authforminterface import Ui_AuthorizationForm
from mainwindow import MainWindow
from registrationform import MainRegistration
import sqlite3

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox


class MainAutorization(QMainWindow, Ui_AuthorizationForm):
    def __init__(self):
        super().__init__()
        self.error_msg = None
        self.register_window = None
        self.main_window = None
        self.setupUi(self)
        self.authButton.clicked.connect(self.auth_button_clicked)
        self.user_id = -1
        self.registerButton.clicked.connect(self.register_button_clicked)

    def auth_button_clicked(self):
        username = self.loginTextBox.text()
        password = self.passwordTextBox.text()

        query = f"""SELECT * FROM Users WHERE Username='{username}' AND password='{password}'"""

        con = sqlite3.connect('database.sqlite')
        cursor = con.cursor()

        # try:
        authorizated_user_info = cursor.execute(query).fetchall()

        if len(authorizated_user_info) == 0:
            self.error_msg = QMessageBox()
            self.error_msg.setWindowTitle('Ошибка')
            self.error_msg.setText('Неверное имя пользователя или пароль')
            self.error_msg.show()
            return

        self.statusBar().showMessage('Авторизация успешна')
        self.user_id = authorizated_user_info[0][0]

        con.commit()
        con.close()
        self.open_main_window()
        # except:
        #     self.statusBar().showMessage('Неверное имя пользователя или пароль')
        #     return

    def register_button_clicked(self):
        self.register_window = MainRegistration()
        self.register_window.auth_form = self
        self.register_window.show()
        self.hide()

    def open_main_window(self):
        self.main_window = MainWindow(self.user_id)
        self.main_window.initial_update_info()
        self.main_window.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainAutorization()
    ex.show()
    sys.exit(app.exec())
