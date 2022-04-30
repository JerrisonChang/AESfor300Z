from PyQt6.QtGui import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QTabWidget
from PyQt6.QtCore import Qt

import sys

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        # super(MainWindow, self).__init__(*args, **kwargs)
        super().__init__()
        self.setWindowTitle("AES")

        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.North)
        self.tabs.setMovable(False)

        for i in ["preprocessing", "postprocessing", "examine"]:
            self.tabs.addTab(QLabel() , i)

        self.setCentralWidget(self.tabs)
        # self.label = QLabel("This IS AWESOME")

        # self.input = QLineEdit()
        # self.input.textChanged.connect(self.label.setText)

        # layout = QVBoxLayout()
        # layout.addWidget(self.input)
        # layout.addWidget(self.label)
        # # label.setAlignment(Qt.AlignCenter)
        # # self.button = QPushButton("Hello")
        # # self.button.setCheckable(True)
        # # self.button.clicked.connect(self.the_button_was_clicked)
        # # self.button.clicked.connect(self.the_button_was_toggled)
        # container = QWidget()
        # container.setLayout(layout)

        # self.setCentralWidget(container)

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)

        self.setWindowTitle("AES done")

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked

        print(f"checked? {self.button_is_checked}")

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

