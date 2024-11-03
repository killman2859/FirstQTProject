from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QComboBox, QHBoxLayout, QSpacerItem

from LessonsType.tasktypetest import Ui_LessonWindow

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication

from random import shuffle


class MainLesson:
    def __init__(self, name_of_lesson, tasks):
        self.tasks = tasks
        self.name_of_lesson = name_of_lesson


class LessonWindowTest(QMainWindow, Ui_LessonWindow):
    def __init__(self, name_of_lesson=""):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f'Урок на тему "{name_of_lesson}"')
        self.answers = dict()
        self.current_iron_button = None
        self.current_russian_button = None
        self.iron_words = list()
        self.russian_words = list()
        self.iron_russian_words = dict()

    def generate_task(self, word_in_the_iron_and_translation={'Some': 'translation'}):
        self.answers = word_in_the_iron_and_translation
        self.iron_words = list(word_in_the_iron_and_translation.keys())
        shuffle(self.iron_words)
        self.russian_words = list(word_in_the_iron_and_translation.values())
        shuffle(self.russian_words)

        for i in range(len(self.iron_words)):
            label = QLabel(self)
            label.setText(self.iron_words[i])
            label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
            some = QComboBox(self)
            some.addItems(self.russian_words)

            horizontal_layout = QHBoxLayout(self)
            horizontal_layout.addWidget(label)
            horizontal_layout.addStretch()
            horizontal_layout.addWidget(some)
            self.allWordsVerticalLayout.addLayout(horizontal_layout)


lesson = None


def initialize_lesson(lesson_name, tasks_of_lesson):
    global lesson

    lesson = MainLesson(lesson_name, tasks_of_lesson)
    for task in lesson.tasks:
        if type(task) is LessonWindowTest:
            task.generate_task()
    lesson.tasks[0].show()
