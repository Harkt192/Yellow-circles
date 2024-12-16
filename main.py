import random
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt6.QtGui import QPainter, QColor


class DrawYellowCircle(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.flag = False
        self.pushButton.clicked.connect(self.draw)

    def initUI(self):
        self.setGeometry(400, 100, 800, 900)
        self.setWindowTitle('Draw circles')

        self.pushButton = QPushButton('Нарисовать', self)
        self.pushButton.move(300, 300)
        self.pushButton.resize(200, 100)
        self.pushButton.setStyleSheet("""
        QPushButton {border-radius: 15px; background-color: #ff9700;}
        QPushButton:hover {background-color: #ff7c00;}
        QPushButton:pressed {background-color: red;}
        """)

    def draw(self):
        self.size = random.randint(30, 100)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(*self.color))
            qp.setBrush(QColor(*self.color))
            self.x, self.y = random.randint(100, 800 - 100), random.randint(100, 900 - 100)
            qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawYellowCircle()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())