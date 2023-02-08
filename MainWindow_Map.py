# Файл с дизайном Главного окна
from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.pushButton_2.setToolTip(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Обновить</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Обновить"))
        self.pushButton.setText(_translate("MainWindow", "Добавить метку"))
        self.Label_name_of_app.setText(_translate("MainWindow",
                                                  "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Перемещайся по карте</span></p></body></html>"))
        self.lineEdit_2.setPlaceholderText(
            _translate("MainWindow", "в градусах"))
        self.Label_latitude.setText(_translate("MainWindow",
                                               "<html><head/><body><p align=\"center\">Широта</p></body></html>"))
        self.Type_of_map.setItemText(0, _translate("MainWindow", "Схема"))
        self.Type_of_map.setItemText(1, _translate("MainWindow", "Спутник"))
        self.Type_of_map.setItemText(2, _translate("MainWindow", "Гибрид"))
        self.lineEdit.setPlaceholderText(
            _translate("MainWindow", "в градусах"))
        self.abel.setText(_translate("MainWindow",
                                     "<html><head/><body><p align=\"center\">Масштаб</p></body></html>"))
        self.Label_longitude.setText(_translate("MainWindow",
                                                "<html><head/><body><p align=\"center\">Долгота</p></body></html>"))
        self.Label_type_of_map.setText(_translate("MainWindow",
                                                  "<html><head/><body><p align=\"center\">Тип карты</p></body></html>"))
        self.lineEdit_4.setPlaceholderText(
            _translate("MainWindow", "в градусах"))
