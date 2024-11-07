import sys
from regisrationforminterface import Ui_RegistrationForm
from mainwindow import MainWindow
import sqlite3

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainRegistration(QMainWindow, Ui_RegistrationForm):
    def __init__(self):
        super().__init__()
        self.auth_form = None
        self.setupUi(self)
        self.registerButton.clicked.connect(self.registration_button_clicked)

    def registration_button_clicked(self):
        name = self.nameTextBox.text()
        surname = self.surnameTextBox.text()
        username = self.loginTextBox.text()
        password = self.passwordTextBox.text()

        query = f"""INSERT INTO Users (ID, Username, Password, Firstname, Secondname) VALUES (Null, '{username}', '{password
        }', '{name}', '{surname}')"""

        querytest = f"SELECT * FROM Users WHERE Username='{username}'"

        con = sqlite3.connect('database.sqlite')
        cursor = con.cursor()

        users_with_login = cursor.execute(querytest).fetchall()

        if len(users_with_login) == 0:
            cursor.execute(query)
        con.commit()
        con.close()
        self.open_auth_form()

    def open_auth_form(self):
        self.auth_form.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainRegistration()
    ex.show()
    sys.exit(app.exec())
