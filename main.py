"""This file is written by me (Rushit Saliya)"""

# imported the built-in n
import sys

# imported following modules to use functionality of PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

# following modules are for generating barcode and qrcode
import pyqrcode
import barcode

# following file is converted from .ui file to .py file to get access of all the elements that we've created by the time of designing in QtDesigner
import LabelGeneratorApplication


class ClassMainDialog(QDialog, LabelGeneratorApplication.Ui_LabelGeneratorApplication):
    """This is the class of our main and only dialog!"""

    def __init__(self):
        # noinspection PyArgumentList
        QDialog.__init__(self)
        self.setupUi(self)      # for loading all the GUI elements in dialog at first
        self.show()

        # to set fixed size and to prevent resizing of dialog just to ensure UI experience
        self.setFixedSize(410, 300)

        # all the event that can be occur
        self.btn_text_insert.clicked.connect(self.update_text)
        self.btn_barcode_generate.clicked.connect(self.set_barcode)
        self.btn_qrcode_generate.clicked.connect(self.set_qrcode)

    # all the event handlers
    def update_text(self):
        """This method is responsible for updating the TEXT label when user press TEXT-INSERT button"""

        self.lbl_text.setText(self.lineEdit.text())

    def set_barcode(self):
        """This event handler is for generating barcode and setting it on its appropriate place"""

        self.generate_barcode()    # this method call is generating the barcode
        self.lbl_barcode_image.setPixmap(QPixmap("barcode.svg"))    # for placing barcode image at the lbl_barcode_image
        self.lbl_barcode_image.setGeometry(179, 55, 350, 120)   # for setting up x, y coordinates and width, length parameters

    def set_qrcode(self):
        """This event handler is for generating qrcode and setting it on its appropriate place"""

        self.generate_qrcode()      # this method call is generating the qrcode
        self.lbl_qrcode_image.setPixmap(QPixmap("qr_code.png"))     # for placing barcode image at the lbl_qrcode_image
        self.lbl_qrcode_image.setGeometry(285, 23, 690, 190)    # for setting up x, y coordinates and width, length parameters

    # following function is for generating the barcode in the image form
    def generate_barcode(self):
        """This method generates barcode on the bases of string that user has entered"""

        image = barcode.get_barcode_class('ean13')      # selecting appropriate format for generating barcode
        image_bar = image(u'{}'.format(self.lineEdit.text()))     # for formatting entered string to pass it into method
        file = open('barcode.svg', 'wb')    # to save generated barcode
        image_bar.write(file)       # to write generated bars in saved file

    # following function is for generating the qrcode in the form of image (in the ".png" format to be precise)
    def generate_qrcode(self):
        """This method generates qrcode on the bases of string that user has entered"""

        qr = pyqrcode.create(self.lineEdit.text())      # to pass entered string by user which is located in lineEdit
        qr.png("qr_code.png", scale=3)      # to save qrcode into png format (where scale is a parameter for adjusting the size of image)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Label_Generator_Application = ClassMainDialog()     # actual creation of application instance
    Label_Generator_Application.show()      # making the new born instance in action
    app.exec_()
