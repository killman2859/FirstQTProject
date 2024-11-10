import sys
import sqlite3

from mainwindowinterface import Ui_MainWindow
from lessonform import LessonWindowTest, MainLesson, initialize_lesson, LessonWindowImages

from PyQt6.QtWidgets import QApplication, QMainWindow


class Lesson:
    def __init__(self, name_of_lesson, task_classes, user_id, main_window_ref):
        self.name_of_lesson = name_of_lesson
        self.task_classes = task_classes
        self.user_id = user_id
        self.main_window_ref = main_window_ref

    def generate_lesson(self):
        initialize_lesson(self.name_of_lesson, self.task_classes, self.user_id, self.main_window_ref)
        return True


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, user_id):
        super().__init__()
        self.setupUi(self)
        self.lessons = dict()
        self.user_id = user_id

        # Создание уроков в списке
        self.lessons = {"Животные": Lesson("Животные", [LessonWindowImages], user_id,
                                           self)}
        self.init_all_lessons()

        self.pushButton_2.clicked.connect(self.quit_app)
        self.selectLessonButton.clicked.connect(self.open_lesson)

    def init_all_lessons(self):
        self.lessonsComboBox.addItems(self.lessons.keys())

    def open_lesson(self):
        lesson_name = self.lessonsComboBox.currentText()

        # Открытие урока
        if self.lessons[lesson_name].generate_lesson():
            self.hide()

    # Обновление информации о количестве пройденных уроков и имени пользователя
    def initial_update_info(self):
        conn = sqlite3.connect('database.sqlite')
        cur = conn.cursor()
        query1 = f"SELECT PassedLesson FROM PassedLessons WHERE PassedUser = {self.user_id}"

        count_of_lessons = len(cur.execute(query1).fetchall())

        query2 = f"SELECT Firstname, Secondname FROM Users WHERE ID = {self.user_id}"

        firstname, secondname = cur.execute(query2).fetchall()[0]

        conn.commit()
        conn.close()

        self.nameAndSurnameLabel.setText(f"{firstname} {secondname}")

        self.lessonCompletedLabel.setText(str(count_of_lessons))

    def update_info_about_levels(self):
        conn = sqlite3.connect('database.sqlite')
        cur = conn.cursor()
        query1 = f"SELECT PassedLesson FROM PassedLessons WHERE PassedUser = {self.user_id}"

        count_of_lessons = len(cur.execute(query1).fetchall())

        self.lessonCompletedLabel.setText(str(count_of_lessons))

        conn.close()

    def quit_app(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow(1)
    ex.show()
    sys.exit(app.exec())
