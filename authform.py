import sys
from authforminterface import Ui_AuthorizationForm
from mainwindow import MainWindow
import sqlite3

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainAutorization(QMainWindow, Ui_AuthorizationForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.authButton.clicked.connect(self.auth_button_clicked)

    def auth_button_clicked(self):
        username = self.loginTextBox.text()
        password = self.passwordTextBox.text()

        query = f"""SELECT * FROM Users WHERE Username='{username}' AND password='{password}'"""

        con = sqlite3.connect('database.sqlite')
        cursor = con.cursor()

        try:
            authorizated_user_info = cursor.execute(query).fetchall()

            if len(authorizated_user_info) == 0:
                self.statusBar().showMessage('Неверное имя пользователя или пароль')
                return

            self.statusBar().showMessage('Авторизация успешна')

            self.open_main_window()
        except:
            self.statusBar().showMessage('Неверное имя пользователя или пароль')
            return

    def open_main_window(self):
        main_window = MainWindow()
        main_window.show()
        # self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainAutorization()
    ex.show()
    sys.exit(app.exec())