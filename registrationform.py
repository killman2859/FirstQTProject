import sys
from regisrationforminterface import Ui_RegistrationForm
from mainwindow import MainWindow
import sqlite3

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox


class UsernameIsOccupied(Exception):
    pass


class UsernameLengthNotCorrect(Exception):
    pass


class NameNotCorrect(Exception):
    pass


class SurnameNotCorrect(Exception):
    pass


class PasswordNotCorrect(Exception):
    pass


def check_name(name):
    if len(name) < 2:
        raise NameNotCorrect
    for i in name:
        if not i.isalpha():
            raise NameNotCorrect


def check_surname(surname):
    if len(surname) < 2:
        raise SurnameNotCorrect
    for i in surname:
        if not i.isalpha():
            raise SurnameNotCorrect


def check_username(username):
    con = sqlite3.connect('database.sqlite')
    cursor = con.cursor()
    query = f"SELECT * FROM Users WHERE Username='{username}'"
    users_with_login = cursor.execute(query).fetchall()
    con.commit()
    con.close()
    if len(users_with_login) != 0:
        raise UsernameIsOccupied
    if len(username) < 5:
        raise UsernameLengthNotCorrect


def check_password(password):
    if len(password) < 8:
        raise PasswordNotCorrect


class MainRegistration(QMainWindow, Ui_RegistrationForm):
    def __init__(self):
        super().__init__()
        self.error_message = QMessageBox()
        self.error_message.setWindowTitle("Ошибка")
        self.auth_form = None
        self.setupUi(self)
        self.registerButton.clicked.connect(self.registration_button_clicked)

    def registration_button_clicked(self):

        try:
            name = self.nameTextBox.text()
            check_name(name)
            surname = self.surnameTextBox.text()
            check_surname(surname)
            username = self.loginTextBox.text()
            check_username(username)
            password = self.passwordTextBox.text()
            check_password(password)

            query = f"""INSERT INTO Users (ID, Username, Password, Firstname, Secondname) VALUES (Null, '{username}', '{password
            }', '{name}', '{surname}')"""

            con = sqlite3.connect('database.sqlite')
            cursor = con.cursor()

            cursor.execute(query)
            con.commit()
            con.close()
            self.open_auth_form()
        except NameNotCorrect:
            self.error_message.setText("Имя должно быть не более 2-х символов и состоять только из букв.")
            self.error_message.show()
            return
        except SurnameNotCorrect:
            self.error_message.setText("Фамилия должна быть не более 2-х символов и состоять только из букв.")
            self.error_message.show()
            return
        except UsernameLengthNotCorrect:
            self.error_message.setText("Логин должен быть не менее 5 символов.")
            self.error_message.show()
            return
        except UsernameIsOccupied:
            self.error_message.setText("Логин уже занят.")
            self.error_message.show()
            return
        except PasswordNotCorrect:
            self.error_message.setText("Пароль должен быть не менее 8 символов.")
            self.error_message.show()
            return

    def open_auth_form(self):
        self.auth_form.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainRegistration()
    ex.show()
    sys.exit(app.exec())
