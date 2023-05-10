from PySide6.QtCore import (QCoreApplication,
    QMetaObject, QRect
    , Qt)
from PySide6.QtGui import (
    QFont)
from PySide6.QtWidgets import (QComboBox, QGridLayout,
    QLabel, QLineEdit, QPushButton,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(617, 172)
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 601, 151))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.filename = QLineEdit(self.gridLayoutWidget)
        self.filename.setObjectName(u"filename")

        self.gridLayout.addWidget(self.filename, 6, 0, 1, 1)

        self.main_label = QLabel(self.gridLayoutWidget)
        self.main_label.setObjectName(u"main_label")
        font = QFont()
        font.setFamilies([u"MS Sans Serif"])
        font.setPointSize(22)
        self.main_label.setFont(font)

        self.gridLayout.addWidget(self.main_label, 0, 0, 1, 1)

        self.btn_recog = QPushButton(self.gridLayoutWidget)
        self.btn_recog.setObjectName(u"btn_recog")

        self.gridLayout.addWidget(self.btn_recog, 7, 0, 1, 1)

        self.cam = QPushButton(self.gridLayoutWidget)
        self.cam.setObjectName(u"cam")

        self.gridLayout.addWidget(self.cam, 7, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"MS Sans Serif"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.label.setFont(font1)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"color:rgb(159, 159, 159)")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1, Qt.AlignTop)

        self.browse = QPushButton(self.gridLayoutWidget)
        self.browse.setObjectName(u"browse")

        self.gridLayout.addWidget(self.browse, 6, 1, 1, 1)

        self.accurancy = QComboBox(self.gridLayoutWidget)
        self.accurancy.setObjectName(u"accurancy")

        self.gridLayout.addWidget(self.accurancy, 1, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1, Qt.AlignRight)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Identitfy Weapons", None))
        
        self.main_label.setText(QCoreApplication.translate("Dialog", u"Weapon Detector", None))
        self.btn_recog.setText(QCoreApplication.translate("Dialog", u"Detect", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Batch C-15", None))
        self.browse.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.cam.setText(QCoreApplication.translate("Dialog", u"Webcam", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Accuracy", None))
    # retranslateUi
