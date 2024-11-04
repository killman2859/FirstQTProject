from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QComboBox, QHBoxLayout, QSpacerItem

import sqlite3

from LessonsType.tasktypetest import Ui_LessonWindow

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication

from random import shuffle

lesson = None


class MainLesson:
    def __init__(self, name_of_lesson, tasks):
        self.tasks = tasks
        self.name_of_lesson = name_of_lesson
        self.task_references = list()


class LessonWindowTest(QMainWindow, Ui_LessonWindow):
    def __init__(self, name_of_lesson="", id_of_task=0):
        super().__init__()
        self.lesson_ref = None
        self.setupUi(self)
        self.name_of_lesson = name_of_lesson
        self.setWindowTitle(f'Урок на тему "{name_of_lesson}"')

        self.answers = dict()
        self.current_iron_button = None
        self.current_russian_button = None
        self.iron_words = list()
        self.russian_words = list()
        self.iron_russian_words = dict()
        self.id_of_task = id_of_task
        self.main_window_ref = None

        self.getResButton.clicked.connect(self.check_answers)
        self.nextTaskButton.setEnabled(False)
        if self.id_of_task == 0:
            self.prevTaskButton.setEnabled(False)
        self.stopLessonButton.setVisible(False)

        self.stopLessonButton.clicked.connect(self.stop_lesson)

    def generate_task(self, main_lesson_ref, user_id, main_window_ref,
                      word_in_the_iron_and_translation={'Куыдз': 'Собака', 'Гӕды': 'Кошка'}):
        self.main_window_ref = main_window_ref
        self.lesson_ref = main_lesson_ref
        self.user_id = user_id
        self.answers = word_in_the_iron_and_translation
        iron_words_for_generate = list(word_in_the_iron_and_translation.keys())
        shuffle(iron_words_for_generate)
        russian_words_for_generate = list(word_in_the_iron_and_translation.values())
        shuffle(russian_words_for_generate)

        for i in range(len(iron_words_for_generate)):
            label = QLabel(self)
            label.setText(iron_words_for_generate[i])
            label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
            some = QComboBox(self)
            some.addItems(russian_words_for_generate)

            self.russian_words.append(some)
            self.iron_words.append(label)

            horizontal_layout = QHBoxLayout(self)
            horizontal_layout.addWidget(label)
            horizontal_layout.addStretch()
            horizontal_layout.addWidget(some)
            self.allWordsVerticalLayout.addLayout(horizontal_layout)

    def check_answers(self):
        for i in range(len(self.iron_words)):
            if self.answers[self.iron_words[i].text()] == self.russian_words[i].currentText():
                self.iron_words[i].setStyleSheet("QLabel { background-color: green; }")
            else:
                self.iron_words[i].setStyleSheet("QLabel { background-color: red; }")

        self.sender().setVisible(False)
        for i in self.russian_words:
            i.setEnabled(False)

        if self.id_of_task != len(self.lesson_ref.tasks) - 1:
            self.nextTaskButton.setEnabled(True)
        else:
            self.stopLessonButton.setVisible(True)

    def change_data_base_info(self):
        query1 = f"SELECT CountOfPassedLessons FROM Users WHERE ID = {self.user_id}"

        conn = sqlite3.connect('database.sqlite')
        cursor = conn.cursor()
        countfofpassedlessons = cursor.execute(query1).fetchall()[0][0]

        if countfofpassedlessons == 0:
            query2 = f"UPDATE Users SET CountOfPassedLessons = {countfofpassedlessons + 1}  WHERE ID = {self.user_id}"
            cursor.execute(query2)

            query3 = f"SELECT ID FROM Lessons WHERE NameOfLesson = '{self.name_of_lesson}'"
            id_of_lesson = cursor.execute(query3).fetchall()[0][0]

            query4 = f"UPDATE Users SET PassedLessonsName = {id_of_lesson} WHERE ID = {self.user_id}"
            cursor.execute(query4)
        else:
            query3 = f"SELECT PassedLessonsName FROM Users WHERE ID = {self.user_id}"
            passed_lessons = cursor.execute(query3).fetchall()[0][0]

            query4 = f"SELECT ID FROM Lessons WHERE NameOfLesson = '{self.name_of_lesson}'"
            id_of_lesson = cursor.execute(query4).fetchall()[0][0]

            if str(id_of_lesson) not in passed_lessons.split(';'):
                query2 = f"UPDATE Users SET CountOfPassedLessons = {countfofpassedlessons + 1}  WHERE ID = {self.user_id}"
                cursor.execute(query2)

                query5 = f"UPDATE Users SET PassedLessonsName = '{passed_lessons + ';' + str(id_of_lesson)}' WHERE ID = {
                self.user_id}"
                cursor.execute(query5)
            else:
                self.statusbar.showMessage("Занятие пройденно, но количество уроков у пользователя не измененно.")

        conn.commit()
        conn.close()

    def stop_lesson(self):
        self.change_data_base_info()
        self.main_window_ref.show()
        self.main_window_ref.update_info_about_levels()
        self.close()


def initialize_lesson(lesson_name, tasks_of_lesson, user_id, main_window_ref):
    global lesson
    lesson = MainLesson(lesson_name, tasks_of_lesson)
    for task_id in range(len(lesson.tasks)):
        if lesson.tasks[task_id] == LessonWindowTest:
            task_ref = LessonWindowTest(lesson_name, task_id)
            task_ref.generate_task(lesson, user_id, main_window_ref)
            lesson.task_references.append(task_ref)
    lesson.task_references[0].show()