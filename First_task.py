import sys

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

from Dialog_Metka import Ui_Dialog
from MainWindow_Map import Ui_MainWindow


class Metka(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Metka_Show)
        self.pushButton_2.clicked.connect(self.Coordinates)
        self.Coordinates()

    def Update_Picture(self):
        pixmap = QPixmap(self.map_file)
        self.Picture_place.setPixmap(pixmap)

    def Metka_Show(self):
        program = Metka()
        program.show()

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
            self.z = '17'
        if self.Type_of_map.currentText() == 'Схема':
            self.type = 'map'
        elif self.Type_of_map.currentText() == 'Спутник':
            self.type = 'sat'
        elif self.Type_of_map.currentText() == 'Гибрид':
            self.type = 'sat,skl'
        self.getImage()

    def getImage(self):
        api_server = "http://static-maps.yandex.ru/1.x/"
        params = {
            "ll": ",".join([self.lon, self.lat]),
            "z": self.z,
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "l": self.type
        }
        response = requests.get(api_server, params=params)
        if not response:
            self.Picture_place.setText('Ошибка выполнения запроса')
        if self.type == 'map':
            self.map_file = "map.png"
        else:
            self.map_file = "map.jpg"
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        self.Update_Picture()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_D:
            self.lon = str(
                float(self.lon) + (0.0064 * (2 ** (17 - int(self.z)))))
            if float(self.lon) > 179:
                self.lon = '179'
        elif event.key() == Qt.Key_A:
            self.lon = str(
                float(self.lon) - (0.0064 * (2 ** (17 - int(self.z)))))
            if float(self.lon) < -179:
                self.lon = '-179'
        elif event.key() == Qt.Key_W:
            self.lat = str(
                float(self.lat) + (0.0027 * (2 ** (17 - int(self.z)))))
            if float(self.lat) > 89:
                self.lat = '89'
        elif event.key() == Qt.Key_S:
            self.lat = str(
                float(self.lat) - (0.0027 * (2 ** (17 - int(self.z)))))
            if float(self.lat) < -89:
                self.lat = '-89'
        if event.key() == Qt.Key_PageUp and int(self.z) < 17:
            self.z = str(int(self.z) + 1)
        if event.key() == Qt.Key_PageDown and int(self.z) > 0:
            self.z = str(int(self.z) - 1)
        self.getImage()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
