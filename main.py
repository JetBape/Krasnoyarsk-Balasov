import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt


class RandomFigures(QMainWindow):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
