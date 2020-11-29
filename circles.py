import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtWidgets, QtCore, QtGui
from random import randrange, randint

class uimain(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(210, 200, 110, 30))
        self.btn.setCheckable(True)
        self.btn.setObjectName('btn')
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Круги"))
        self.btn.setText(_translate("MainWindow", 'Нарисовать круг'))


class Example(QMainWindow, uimain):
    def __init__(self):
        super().__init__()
        self.ok = False
        self.setupUi(self)
        self.btn.clicked.connect(self.run)

    def run(self):
        self.ok = True
        self.repaint()

    def paintEvent(self, event):
        if self.ok:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        a1 = randint(0, 255)
        a2 = randint(0, 255)
        a3 = randint(0, 255)
        qp.setBrush(QColor(a1, a2, a3))
        a = randint(30, 120)
        qp.drawEllipse(randrange(self.height() - a), randrange(self.width() - a), a, a)
        self.ok = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())