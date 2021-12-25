import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

ERRS = ["Another useless circle...", "Stop doing useless things", "You waste your time!",
        "You better stop doing that", "Useless at the top!", "The last circle was even less useless than this one!",
        "Close the window!", "You mess me up!"]


class Window(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(396, 252)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(86, 10, 209, 23))
        self.errr = QLabel(Form)
        self.errr.setObjectName(u"errr")
        self.errr.setGeometry(QRect(10, 228, 379, 25))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 35, 202, 16))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c \u0431\u0435\u0441\u043f\u043e\u043b\u0435\u0437\u043d\u0443\u044e \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.errr.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041e\u043d\u0430 \u0431\u0443\u0434\u0435\u0442 \u0433\u0434\u0435-\u0442\u043e \u0442\u0443\u0442", None))

class App(Window, QMainWindow):
    draw = False

    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Useless circles 2. More useless than past ones")
        self.pushButton.clicked.connect(self.enable)

    def paintEvent(self, qp: QPainter):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            self.draw_useless_circle_for_free(qp)
            qp.end()

    def draw_useless_circle_for_free(self, qp: QPainter):
        self.label_2.setText(__import__("random").choice(ERRS))
        qp.setBrush(QColor(__import__("random").randrange(0, 256), __import__("random").randrange(0, 256), __import__("random").randrange(0, 256)))
        qp.drawEllipse(200, 75, *(__import__('random').randrange(0, 100),) * 2)

    def enable(self):
        self.draw = True
        self.repaint()


if __name__ == '__main__':
    a = QApplication(sys.argv)
    b = App()
    b.show()
    sys.exit(a.exec())
