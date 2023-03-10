import sys

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

from MainWindow_Map import Ui_API_PROJECT

class MyWidget(QMainWindow, Ui_API_PROJECT):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lon = '37.530887'
        self.lat = '55.703118'
        self.z = '17'
        self.address = ''
        self.index = 'индекс'
        self.New_Coordinates()
        self.pushButton_3.clicked.connect(self.getObject)
        self.pushButton_2.clicked.connect(self.New_Coordinates)
        self.pushButton.clicked.connect(self.getOrganization)
        self.checkBox.clicked.connect(self.Address_hide_or_show)

    def getOrganization(self):
        txt = self.lineEdit_5.text()
        search_api_server = "https://search-maps.yandex.ru/v1/"
        api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

        address_ll = ",".join([self.lon, self.lat])

        search_params = {
            "apikey": api_key,
            "text": txt,
            "lang": "ru_RU",
            "ll": address_ll,
            "type": "biz"
        }

        response = requests.get(search_api_server, params=search_params)
        if not response:
            self.Picture_place.setText('Ошибка выполнения запроса')
        json_response = response.json()

        organization = json_response["features"][0]
        self.org_address = organization["properties"]["CompanyMetaData"]["address"]
        self.address = self.org_address

        point = organization["geometry"]["coordinates"]
        self.lon, self.lat = point[0], point[1]
        org_point = "{0},{1}".format(point[0], point[1])
        map_params = {
            "ll": org_point,
            "z": self.z,
            "l": self.type,
            "pt": "{0},ya_ru".format(org_point)
        }

        map_api_server = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(map_api_server, params=map_params)

        with open(self.map_file, "wb") as file:
            file.write(response.content)
        self.Update_Picture()

    def Update_Picture(self):
        pixmap = QPixmap(self.map_file)
        self.Picture_place.setPixmap(pixmap)
        self.lineEdit_6.setText(self.address)

    def New_Coordinates(self):
        if self.lineEdit.text() != '':
            self.lon = self.lineEdit.text()
        if self.lineEdit_2.text() != '':
            self.lat = self.lineEdit_2.text()
        if self.lineEdit_4.text() != '':
            self.z = self.lineEdit_4.text()
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

    def getObject(self):
        toponym_to_find = self.lineEdit_3.text()
        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": toponym_to_find,
            "format": "json"}

        response = requests.get(geocoder_api_server, params=geocoder_params)
        if not response:
            self.Picture_place.setText('Ошибка выполнения запроса')

        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        toponym_coodrinates = toponym["Point"]["pos"]
        self.toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
        self.lon, self.lat = toponym_coodrinates.split(" ")
        map_params = {
            "ll": ",".join([self.lon, self.lat]),
            "z": self.z,
            "l": self.type,
            "pt": "{0},ya_ru".format(",".join([self.lon, self.lat]))
        }

        self.address = self.toponym_address

        map_api_server = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(map_api_server, params=map_params)

        with open(self.map_file, "wb") as file:
            file.write(response.content)
        self.Update_Picture()

    def Address_hide_or_show(self):
        if self.checkBox.isChecked():
            self.lineEdit_6.setText(f'{self.address}, {self.index}')
        else:
            self.lineEdit_6.setText(self.address)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
