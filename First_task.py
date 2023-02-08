import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import requests


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 499)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 9, 0, 4, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 8, 0, 1, 1)
        self.Label_name_of_app = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Label_name_of_app.setFont(font)
        self.Label_name_of_app.setObjectName("Label_name_of_app")
        self.gridLayout.addWidget(self.Label_name_of_app, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 5, 0, 1, 1)
        self.Label_latitude = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Label_latitude.setFont(font)
        self.Label_latitude.setObjectName("Label_latitude")
        self.gridLayout.addWidget(self.Label_latitude, 4, 0, 1, 1)
        self.Type_of_map = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.Type_of_map.setFont(font)
        self.Type_of_map.setObjectName("Type_of_map")
        self.Type_of_map.addItem("")
        self.Type_of_map.addItem("")
        self.Type_of_map.addItem("")
        self.gridLayout.addWidget(self.Type_of_map, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 1)
        self.abel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.abel.setFont(font)
        self.abel.setObjectName("abel")
        self.gridLayout.addWidget(self.abel, 6, 0, 1, 1)
        self.Picture_place = QtWidgets.QLabel(self.centralwidget)
        self.Picture_place.setMinimumSize(QtCore.QSize(600, 450))
        self.Picture_place.setMaximumSize(QtCore.QSize(600, 450))
        self.Picture_place.setFrameShape(QtWidgets.QFrame.Box)
        self.Picture_place.setText("")
        self.Picture_place.setObjectName("Picture_place")
        self.gridLayout.addWidget(self.Picture_place, 1, 1, 12, 1)
        self.Label_longitude = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Label_longitude.setFont(font)
        self.Label_longitude.setObjectName("Label_longitude")
        self.gridLayout.addWidget(self.Label_longitude, 2, 0, 1, 1)
        self.Label_type_of_map = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Label_type_of_map.setFont(font)
        self.Label_type_of_map.setObjectName("Label_type_of_map")
        self.gridLayout.addWidget(self.Label_type_of_map, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 7, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Обновить</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Обновить"))
        self.pushButton.setText(_translate("MainWindow", "Добавить метку"))
        self.Label_name_of_app.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Перемещайся по карте</span></p></body></html>"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "в градусах"))
        self.Label_latitude.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Широта</p></body></html>"))
        self.Type_of_map.setItemText(0, _translate("MainWindow", "Схема"))
        self.Type_of_map.setItemText(1, _translate("MainWindow", "Спутник"))
        self.Type_of_map.setItemText(2, _translate("MainWindow", "Гибрид"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "в градусах"))
        self.abel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Масштаб</p></body></html>"))
        self.Label_longitude.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Долгота</p></body></html>"))
        self.Label_type_of_map.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Тип карты</p></body></html>"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "в градусах"))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 230)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 130, 41, 41))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Metka_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 180, 41, 41))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Metka_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 130, 41, 41))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Metka_3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(80, 180, 41, 41))
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Metka_4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 130, 41, 41))
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Metka_5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 180, 41, 41))
        self.pushButton_6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Metka_6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 90, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "в градусах"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "в градусах"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Долгота</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Широта</span></p></body></html>"))


class Metka(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Metka_Show)
        self.pushButton_2.clicked.connect(self.getImage)
        self.Coordinates()
        self.getImage()

    def Update_Picture(self):
        self.pixmap = QtGui.QPixmap(self.map_file)
        self.Picture_place.setPixmap(self.pixmap)

    def Metka_Show(self):
        self.program = Metka()
        self.program.show()

    def Coordinates(self):
        if self.lineEdit.text() != '':
            self.lon = self.lineEdit.text()
        else:
            self.lon = '37.530887'
        if self.lineEdit_2.text() != '':
            self.lat = self.lineEdit_2.text()
        else:
            self.lat = '55.703118'
        if self.lineEdit_4.text() != '':
            self.z = self.lineEdit_4.text()
        else:
            self.z = '14'
        if self.Type_of_map.currentText() == 'Схема':
            self.type = 'map'
        elif self.Type_of_map.currentText() == 'Спутник':
            self.type = 'sat'
        elif self.Type_of_map.currentText() == 'Гибрид':
            self.type = 'sat,skl'

    def getImage(self):
        api_server = "http://static-maps.yandex.ru/1.x/"
        params = {
            "ll": ",".join([self.lon, self.lat]),
            "z": self.z,
            "l": self.type,
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b"
        }
        response = requests.get(api_server, params=params)
        if not response:
            self.Picture_place.setText('Ошибка выполнения запроса')
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        self.Update_Picture()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_D:
            self.lon = str(float(self.lon) + 1)
        if event.key() == Qt.Key_A:
            self.lon = str(float(self.lon) - 1)
        if event.key() == Qt.Key_W:
            self.lat = str(float(self.lat) + 1)
        if event.key() == Qt.Key_S:
            self.lat = str(float(self.lat) - 1)
        if event.key() == Qt.Key_PageUp:
            self.z = str(int(self.z) + 1)
            if int(self.z) > 14:
                self.z = '14'
        if event.key() == Qt.Key_PageDown:
            self.z = str(int(self.z) - 1)
            if int(self.z) < 0:
                self.z = '0'
        self.getImage()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
