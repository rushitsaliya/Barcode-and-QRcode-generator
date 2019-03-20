"""This file is generated from LabelGeneratorApplication.ui file with the help of pyuic5.exe tool"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\LabelGeneratorApplication.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LabelGeneratorApplication(object):
    def setupUi(self, LabelGeneratorApplication):
        LabelGeneratorApplication.setObjectName("LabelGeneratorApplication")
        LabelGeneratorApplication.resize(407, 288)
        self.lbl_title = QtWidgets.QLabel(LabelGeneratorApplication)
        self.lbl_title.setGeometry(QtCore.QRect(60, 20, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.lbl_text = QtWidgets.QLabel(LabelGeneratorApplication)
        self.lbl_text.setGeometry(QtCore.QRect(30, 80, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_text.setFont(font)
        self.lbl_text.setObjectName("lbl_text")
        self.lbl_enter_text = QtWidgets.QLabel(LabelGeneratorApplication)
        self.lbl_enter_text.setGeometry(QtCore.QRect(10, 170, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_enter_text.setFont(font)
        self.lbl_enter_text.setObjectName("lbl_enter_text")
        self.lineEdit = QtWidgets.QLineEdit(LabelGeneratorApplication)
        self.lineEdit.setGeometry(QtCore.QRect(130, 170, 261, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.btn_text_insert = QtWidgets.QPushButton(LabelGeneratorApplication)
        self.btn_text_insert.setGeometry(QtCore.QRect(44, 220, 81, 41))
        self.btn_text_insert.setObjectName("btn_text_insert")
        self.btn_barcode_generate = QtWidgets.QPushButton(LabelGeneratorApplication)
        self.btn_barcode_generate.setGeometry(QtCore.QRect(160, 220, 91, 41))
        self.btn_barcode_generate.setObjectName("btn_barcode_generate")
        self.btn_qrcode_generate = QtWidgets.QPushButton(LabelGeneratorApplication)
        self.btn_qrcode_generate.setGeometry(QtCore.QRect(274, 220, 81, 41))
        self.btn_qrcode_generate.setObjectName("btn_qrcode_generate")
        self.lbl_barcode_image = QtWidgets.QLabel(LabelGeneratorApplication)
        self.lbl_barcode_image.setGeometry(QtCore.QRect(170, 92, 81, 61))
        self.lbl_barcode_image.setObjectName("lbl_barcode_image")
        self.lbl_qrcode_image = QtWidgets.QLabel(LabelGeneratorApplication)
        self.lbl_qrcode_image.setGeometry(QtCore.QRect(310, 90, 61, 61))
        self.lbl_qrcode_image.setObjectName("lbl_qrcode_image")
        self.lbl_enter_text.setBuddy(self.lineEdit)

        self.retranslateUi(LabelGeneratorApplication)
        QtCore.QMetaObject.connectSlotsByName(LabelGeneratorApplication)
        LabelGeneratorApplication.setTabOrder(self.lineEdit, self.btn_text_insert)
        LabelGeneratorApplication.setTabOrder(self.btn_text_insert, self.btn_barcode_generate)
        LabelGeneratorApplication.setTabOrder(self.btn_barcode_generate, self.btn_qrcode_generate)

    def retranslateUi(self, LabelGeneratorApplication):
        _translate = QtCore.QCoreApplication.translate
        LabelGeneratorApplication.setWindowTitle(_translate("LabelGeneratorApplication", "Label Generator Application"))
        self.lbl_title.setText(_translate("LabelGeneratorApplication", "Label Generator Application"))
        self.lbl_text.setText(_translate("LabelGeneratorApplication", "<html><head/><body><p>Text</p></body></html>"))
        self.lbl_enter_text.setText(_translate("LabelGeneratorApplication", "ENTER TEXT"))
        self.lineEdit.setPlaceholderText(_translate("LabelGeneratorApplication", "FOR EX. 123456789 ABCDEF......"))
        self.btn_text_insert.setText(_translate("LabelGeneratorApplication", "TEXT INSERT"))
        self.btn_barcode_generate.setText(_translate("LabelGeneratorApplication", "BARCODE\n"
"GENERATE"))
        self.btn_qrcode_generate.setText(_translate("LabelGeneratorApplication", "QRCODE\n"
"GENERATE"))
        self.lbl_barcode_image.setText(_translate("LabelGeneratorApplication", "<html><head/><body><p><span style=\" font-size:12pt;\">Barcode</span></p><p><span style=\" font-size:12pt;\">Image</span></p></body></html>"))
        self.lbl_qrcode_image.setText(_translate("LabelGeneratorApplication", "<html><head/><body><p><span style=\" font-size:12pt;\">QRcode</span></p><p><span style=\" font-size:12pt;\">Image</span></p></body></html>"))

