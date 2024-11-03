import sys
from mainwindowinterface import Ui_MainWindow
from lessonform import LessonWindowTest, MainLesson, initialize_lesson

from PyQt6.QtWidgets import QApplication, QMainWindow



class Lesson:
    def __init__(self, name_of_lesson, task_classes):
        self.name_of_lesson = name_of_lesson
        self.task_classes = task_classes

    def generate_lesson(self):
        initialize_lesson(self.name_of_lesson, self.task_classes)
        return True


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lessons = dict()
        self.lessons = {"Животные": Lesson("Животные", [LessonWindowTest("Животные")])}
        self.init_all_lessons()

        self.selectLessonButton.clicked.connect(self.open_lesson)

    def init_all_lessons(self):
        self.lessonsComboBox.addItems(self.lessons.keys())

    def open_lesson(self):
        lesson_name = self.lessonsComboBox.currentText()
        if self.lessons[lesson_name].generate_lesson():
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
