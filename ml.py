import sys
import random
from PyQt5 import Qt, QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class EscapeButton(QPushButton):
    mouseMoved = pyqtSignal()

    def mouseMoveEvent(self, event):
        self.mouseMoved.emit()


class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.coords = [360, 290]
        self.btn_size = [120, 26]
        self.w = 600
        self.h = 350

        self.setGeometry(660, 365, self.w, self.h)
        self.setWindowTitle('For my love')

        self.letter = QLabel('<font color="purple">Будешь ли моей половинкой 14 февраля?</font>', self)
        self.letter.setFont(Qt.QFont('abc', 11))
        self.letter.move(155, 260)

        self.yes_btn = QPushButton('Конечно!', self)
        self.yes_btn.resize(*self.btn_size)
        self.yes_btn.move(120, 290)
        self.yes_btn.clicked.connect(self.changeGif)

        self.label = QLabel(self)
        self.label.resize(600, 300)
        self.label.move(140, -30)
        path = 'gif1.gif'
        gif = QtGui.QMovie(path)
        self.label.setMovie(gif)
        gif.start()

        self.escp_btn = EscapeButton('Нет, я буду занята.', self)
        self.escp_btn.setMouseTracking(True)
        self.escp_btn.resize(*self.btn_size)
        self.escp_btn.move(*self.coords)
        self.escp_btn.mouseMoved.connect(self.moveButton)

    def moveButton(self):
        self.coords[0] = random.randint(0, self.w - self.btn_size[0])
        self.coords[1] = random.randint(0, self.h - self.btn_size[1])
        self.escp_btn.move(*self.coords)

    def changeGif(self):
        path = 'gif2.gif'
        gif = QtGui.QMovie(path)
        self.label.setMovie(gif)
        gif.start()

        self.escp_btn.hide()
        self.yes_btn.hide()

        self.letter.move(250, 280)
        self.letter.setText('<font color="purple">Люблю тебя ❤️</font>')
        self.letter.setFont(Qt.QFont('abc', 13))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
