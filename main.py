import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication

from ui_file import Ui_Form


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Git и цветные окружности')
        self.pushBut.clicked.connect(self.butPressEvent)

    def butPressEvent(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            for i in range(randint(1, 5)):
                qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
                size = randint(1, 350)
                x, y = randint(0, self.size().width()), randint(0, self.size().height())
                qp.drawEllipse(x - size // 2, y - size // 2, size, size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
