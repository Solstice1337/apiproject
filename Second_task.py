import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import requests


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 474)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Picture_place = QtWidgets.QLabel(self.centralwidget)
        self.Picture_place.setMinimumSize(QtCore.QSize(600, 450))
        self.Picture_place.setMaximumSize(QtCore.QSize(600, 450))
        self.Picture_place.setFrameShape(QtWidgets.QFrame.Box)
        self.Picture_place.setText("")
        self.Picture_place.setObjectName("Picture_place")
        self.gridLayout.addWidget(self.Picture_place, 0, 0, 2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.z = '0'
        self.lon = '37.620070'
        self.lat = '55.753630'
        self.peredvig_up_down = 0
        self.peredvig_right_left = 0
        self.getImage()

    def Update_Picture(self):
        self.pixmap = QtGui.QPixmap(self.map_file)
        self.Picture_place.setPixmap(self.pixmap)

    def getImage(self):
        api_server = "http://static-maps.yandex.ru/1.x/"
        params = {
            "ll": ",".join([self.lon,self.lat]),
            "l": 'map',
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b"
        }
        response = requests.get(api_server,params=params)
        if not response:
            self.Picture_place.setText('Ошибка выполнения запроса')
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        self.Update_Picture()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_D:
            if self.peredvig_up_down <= 20:
                self.lon = str(float(self.lon) + 1)
                self.peredvig_up_down += 1
        if event.key() == QtCore.Qt.Key_A:
            if self.peredvig_up_down >= -20:
                self.lon = str(float(self.lon) - 1)
                self.peredvig_up_down -= 1
        if event.key() == QtCore.Qt.Key_W:
            if self.peredvig_right_left <= 20:
                self.lat = str(float(self.lat) + 1)
                self.peredvig_right_left += 1
        if event.key() == QtCore.Qt.Key_S:
            if self.peredvig_right_left >= -20:
                self.lat = str(float(self.lat) - 1)
                self.peredvig_right_left -= 1
        self.getImage()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())