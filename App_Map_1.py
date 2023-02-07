from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
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



class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.getImage()

    def getImage(self):
        map_request = "http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn=0.002,0.002&l=map"
        response = requests.get(map_request)
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:",response.status_code,"(",response.reason,")")
            sys.exit(1)
        self.map_file = "map.png"
        with open(self.map_file,"wb") as file:
            file.write(response.content)

    def initUI(self):
        self.pixmap = QPixmap(self.map_file)
        self.Picture_place.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())