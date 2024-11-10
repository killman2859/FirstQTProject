import sqlite3
from random import shuffle, sample

from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QLabel, QComboBox, QHBoxLayout, QVBoxLayout

from LessonsType.tasktypetest import Ui_LessonWindow
from LessonsType.tasktypeimages import Ui_LessonWindowImages

lesson = None


def read_database_info():
    conn = sqlite3.connect('database.sqlite')
    cur = conn.cursor()
    query = f"SELECT * FROM IronWords WHERE LessonID = 1"
    word_list_from_db = sample(cur.execute(query).fetchall(), 4)
    conn.commit()
    conn.close()

    return word_list_from_db


class MainLesson:
    def __init__(self, name_of_lesson, tasks):
        self.tasks = tasks
        self.name_of_lesson = name_of_lesson
        self.task_references = list()


class LessonWindowTest(QMainWindow, Ui_LessonWindow):
    def __init__(self, name_of_lesson="", id_of_task=0):
        super().__init__()
        self.setupUi(self)
        self.name_of_lesson = name_of_lesson
        self.setWindowTitle(f'Урок на тему "{name_of_lesson}"')

        self.answers = dict()
        self.lesson_ref = None
        self.current_iron_button = None
        self.current_russian_button = None
        self.iron_words = list()
        self.russian_words = list()
        self.id_of_task = id_of_task
        self.main_window_ref = None

        self.getResButton.clicked.connect(self.check_answers)
        self.nextTaskButton.setEnabled(False)
        if self.id_of_task == 0:
            self.prevTaskButton.setEnabled(False)
        self.stopLessonButton.setVisible(False)

        self.stopLessonButton.clicked.connect(self.stop_lesson)

    def generate_task(self, main_lesson_ref, user_id, main_window_ref):

        # Считываем данные с ДБ
        word_list_from_db = read_database_info()

        # Заполняем словарь словами и переводами из БД
        for word in word_list_from_db:
            self.answers[word[2]] = word[3]

        self.main_window_ref = main_window_ref
        self.lesson_ref = main_lesson_ref
        self.user_id = user_id
        iron_words_for_generate = list(self.answers.keys())
        shuffle(iron_words_for_generate)
        russian_words_for_generate = list(self.answers.values())
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

        conn = sqlite3.connect('database.sqlite')
        cursor = conn.cursor()

        query1 = f"SELECT ID FROM Lessons WHERE Name='{self.lesson_ref.name_of_lesson}'"

        lesson_id = cursor.execute(query1).fetchone()[0]

        query = f"INSERT INTO PassedLessons(ID, PassedUser, PassedLesson) VALUES(NULL, {self.user_id}, {lesson_id})"
        query2 = f"SELECT ID FROM PassedLessons WHERE ID = {self.user_id} AND PassedLesson = {lesson_id}"
        passed_lesson_with_current_id = cursor.execute(query2).fetchall()

        if len(passed_lesson_with_current_id) == 0:
            cursor.execute(query)
        else:
            self.statusbar.showMessage("Урок уже пройден")

        conn.commit()
        conn.close()

    def stop_lesson(self):
        self.change_data_base_info()
        self.main_window_ref.show()
        self.main_window_ref.update_info_about_levels()
        self.close()

    def __str__(self):
        return f'LessonWindowTest'


# Image size 176x176 pixels
class LessonWindowImages(QMainWindow, Ui_LessonWindowImages):
    def __init__(self, name_of_lesson="", id_of_task=0):
        super().__init__()
        self.setupUi(self)
        self.name_of_lesson = name_of_lesson
        self.setWindowTitle(f'Урок на тему "{name_of_lesson}"')

        self.answers = dict()
        self.answers_refs = dict()
        self.lesson_ref = None
        self.id_of_task = id_of_task
        self.main_window_ref = None

        self.getResButton.clicked.connect(self.check_answers)
        self.nextTaskButton.setEnabled(False)
        if self.id_of_task == 0:
            self.prevTaskButton.setEnabled(False)
        self.stopLessonButton.setVisible(False)

        self.stopLessonButton.clicked.connect(self.stop_lesson)

    def generate_task(self, main_lesson_ref, user_id, main_window_ref):
        # Считываем данные с ДБ
        word_list_from_db = read_database_info()

        # Заполняем словарь словами и переводами из БД
        for word in word_list_from_db:
            self.answers[word[4]] = word[2]

        # Создание интерфейса
        for i in range(len(self.answers.keys())):
            label = QLabel(self)
            label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            pixmap = QPixmap('Images/' + str(list(self.answers.keys())[i]))
            label.setPixmap(pixmap)
            verticallayout = QVBoxLayout()
            verticallayout.addWidget(label)

            allwords = QComboBox(self)
            allwords.addItems(list(self.answers.values()))
            verticallayout.addWidget(allwords)

            self.answers_refs[label] = allwords

            self.horizontalLayout.addLayout(verticallayout)

    def check_answers(self):
        pass

    def stop_lesson(self):
        pass


tasks_names = {LessonWindowTest: "LessonWindowTest", LessonWindowImages: "LessonWindowImages"}


def initialize_lesson(lesson_name, tasks_of_lesson, user_id, main_window_ref):
    global lesson
    lesson = MainLesson(lesson_name, tasks_of_lesson)
    for task_id in range(len(lesson.tasks)):
        task_ref = eval(tasks_names[lesson.tasks[task_id]] + '(lesson_name, task_id)')
        task_ref.generate_task(lesson, user_id, main_window_ref)
        lesson.task_references.append(task_ref)

    lesson.task_references[0].show()
