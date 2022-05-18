# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1819, 998)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1600, 848))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.setObjectName(u"actionOpen_File")
        self.actionOpen_Folder = QAction(MainWindow)
        self.actionOpen_Folder.setObjectName(u"actionOpen_Folder")
        self.actionExport_template = QAction(MainWindow)
        self.actionExport_template.setObjectName(u"actionExport_template")
        self.actionEnter_License_Key = QAction(MainWindow)
        self.actionEnter_License_Key.setObjectName(u"actionEnter_License_Key")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.listWidget, 0, 0, 6, 1)

        self.groupBox_template = QGroupBox(self.centralwidget)
        self.groupBox_template.setObjectName(u"groupBox_template")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_template.sizePolicy().hasHeightForWidth())
        self.groupBox_template.setSizePolicy(sizePolicy3)
        self.groupBox_template.setMinimumSize(QSize(450, 200))
        self.pushButton_template = QPushButton(self.groupBox_template)
        self.pushButton_template.setObjectName(u"pushButton_template")
        self.pushButton_template.setGeometry(QRect(50, 20, 141, 28))
        self.textEdit_template = QTextEdit(self.groupBox_template)
        self.textEdit_template.setObjectName(u"textEdit_template")
        self.textEdit_template.setGeometry(QRect(10, 60, 381, 121))
        self.pushButton_export_template = QPushButton(self.groupBox_template)
        self.pushButton_export_template.setObjectName(u"pushButton_export_template")
        self.pushButton_export_template.setGeometry(QRect(220, 20, 141, 28))

        self.gridLayout.addWidget(self.groupBox_template, 3, 2, 1, 1)

        self.groupBox_barcode = QGroupBox(self.centralwidget)
        self.groupBox_barcode.setObjectName(u"groupBox_barcode")
        sizePolicy3.setHeightForWidth(self.groupBox_barcode.sizePolicy().hasHeightForWidth())
        self.groupBox_barcode.setSizePolicy(sizePolicy3)
        self.groupBox_barcode.setMinimumSize(QSize(450, 220))
        self.groupBox_4 = QGroupBox(self.groupBox_barcode)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 20, 431, 111))
        self.checkBox_code39 = QCheckBox(self.groupBox_4)
        self.checkBox_code39.setObjectName(u"checkBox_code39")
        self.checkBox_code39.setGeometry(QRect(50, 20, 81, 20))
        self.checkBox_code39.setChecked(True)
        self.checkBox_code93 = QCheckBox(self.groupBox_4)
        self.checkBox_code93.setObjectName(u"checkBox_code93")
        self.checkBox_code93.setGeometry(QRect(130, 20, 81, 20))
        self.checkBox_code93.setChecked(True)
        self.checkBox_code128 = QCheckBox(self.groupBox_4)
        self.checkBox_code128.setObjectName(u"checkBox_code128")
        self.checkBox_code128.setGeometry(QRect(210, 20, 81, 20))
        self.checkBox_code128.setChecked(True)
        self.checkBox_codabar = QCheckBox(self.groupBox_4)
        self.checkBox_codabar.setObjectName(u"checkBox_codabar")
        self.checkBox_codabar.setGeometry(QRect(300, 20, 81, 20))
        self.checkBox_codabar.setChecked(True)
        self.checkBox_itf = QCheckBox(self.groupBox_4)
        self.checkBox_itf.setObjectName(u"checkBox_itf")
        self.checkBox_itf.setGeometry(QRect(50, 50, 81, 20))
        self.checkBox_itf.setChecked(True)
        self.checkBox_ean13 = QCheckBox(self.groupBox_4)
        self.checkBox_ean13.setObjectName(u"checkBox_ean13")
        self.checkBox_ean13.setGeometry(QRect(130, 50, 81, 20))
        self.checkBox_ean13.setChecked(True)
        self.checkBox_ean8 = QCheckBox(self.groupBox_4)
        self.checkBox_ean8.setObjectName(u"checkBox_ean8")
        self.checkBox_ean8.setGeometry(QRect(210, 50, 81, 20))
        self.checkBox_ean8.setChecked(True)
        self.checkBox_upca = QCheckBox(self.groupBox_4)
        self.checkBox_upca.setObjectName(u"checkBox_upca")
        self.checkBox_upca.setGeometry(QRect(300, 50, 81, 20))
        self.checkBox_upca.setChecked(True)
        self.checkBox_upce = QCheckBox(self.groupBox_4)
        self.checkBox_upce.setObjectName(u"checkBox_upce")
        self.checkBox_upce.setGeometry(QRect(50, 80, 81, 20))
        self.checkBox_upce.setChecked(True)
        self.checkBox_industrial25 = QCheckBox(self.groupBox_4)
        self.checkBox_industrial25.setObjectName(u"checkBox_industrial25")
        self.checkBox_industrial25.setGeometry(QRect(130, 80, 101, 20))
        self.checkBox_industrial25.setChecked(True)
        self.groupBox_5 = QGroupBox(self.groupBox_barcode)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(9, 139, 431, 71))
        self.groupBox_5.setMinimumSize(QSize(150, 40))
        self.checkBox_qrcode = QCheckBox(self.groupBox_5)
        self.checkBox_qrcode.setObjectName(u"checkBox_qrcode")
        self.checkBox_qrcode.setGeometry(QRect(50, 10, 81, 20))
        self.checkBox_qrcode.setChecked(True)
        self.checkBox_pdf417 = QCheckBox(self.groupBox_5)
        self.checkBox_pdf417.setObjectName(u"checkBox_pdf417")
        self.checkBox_pdf417.setGeometry(QRect(140, 10, 81, 20))
        self.checkBox_pdf417.setChecked(True)
        self.checkBox_aztec = QCheckBox(self.groupBox_5)
        self.checkBox_aztec.setObjectName(u"checkBox_aztec")
        self.checkBox_aztec.setGeometry(QRect(220, 10, 81, 20))
        self.checkBox_aztec.setChecked(True)
        self.checkBox_postalcode = QCheckBox(self.groupBox_5)
        self.checkBox_postalcode.setObjectName(u"checkBox_postalcode")
        self.checkBox_postalcode.setGeometry(QRect(320, 10, 91, 20))
        self.checkBox_postalcode.setChecked(True)
        self.checkBox_maxicode = QCheckBox(self.groupBox_5)
        self.checkBox_maxicode.setObjectName(u"checkBox_maxicode")
        self.checkBox_maxicode.setGeometry(QRect(50, 40, 81, 20))
        self.checkBox_maxicode.setChecked(True)
        self.checkBox_dotcode = QCheckBox(self.groupBox_5)
        self.checkBox_dotcode.setObjectName(u"checkBox_dotcode")
        self.checkBox_dotcode.setGeometry(QRect(140, 40, 81, 20))
        self.checkBox_dotcode.setChecked(True)
        self.checkBox_patchcode = QCheckBox(self.groupBox_5)
        self.checkBox_patchcode.setObjectName(u"checkBox_patchcode")
        self.checkBox_patchcode.setGeometry(QRect(220, 40, 91, 20))
        self.checkBox_patchcode.setChecked(True)
        self.checkBox_datamatrix = QCheckBox(self.groupBox_5)
        self.checkBox_datamatrix.setObjectName(u"checkBox_datamatrix")
        self.checkBox_datamatrix.setGeometry(QRect(320, 40, 91, 20))
        self.checkBox_datamatrix.setChecked(True)
        self.checkBox_gs1 = QCheckBox(self.groupBox_5)
        self.checkBox_gs1.setObjectName(u"checkBox_gs1")
        self.checkBox_gs1.setGeometry(QRect(50, 70, 121, 20))
        self.checkBox_gs1.setChecked(True)

        self.gridLayout.addWidget(self.groupBox_barcode, 4, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setMinimumSize(QSize(800, 800))
        self.label.setMaximumSize(QSize(4096, 4096))
        self.label.setMouseTracking(True)

        self.gridLayout.addWidget(self.label, 0, 1, 6, 1)

        self.textEdit_results = QTextEdit(self.centralwidget)
        self.textEdit_results.setObjectName(u"textEdit_results")
        sizePolicy2.setHeightForWidth(self.textEdit_results.sizePolicy().hasHeightForWidth())
        self.textEdit_results.setSizePolicy(sizePolicy2)
        self.textEdit_results.setMinimumSize(QSize(450, 200))

        self.gridLayout.addWidget(self.textEdit_results, 5, 2, 1, 1)

        self.groupBox_camera = QGroupBox(self.centralwidget)
        self.groupBox_camera.setObjectName(u"groupBox_camera")
        sizePolicy3.setHeightForWidth(self.groupBox_camera.sizePolicy().hasHeightForWidth())
        self.groupBox_camera.setSizePolicy(sizePolicy3)
        self.groupBox_camera.setMinimumSize(QSize(450, 150))
        self.comboBox = QComboBox(self.groupBox_camera)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(180, 50, 101, 31))
        self.label_2 = QLabel(self.groupBox_camera)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 50, 131, 31))
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.pushButton_open = QPushButton(self.groupBox_camera)
        self.pushButton_open.setObjectName(u"pushButton_open")
        self.pushButton_open.setGeometry(QRect(90, 90, 93, 28))
        self.pushButton_stop = QPushButton(self.groupBox_camera)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setGeometry(QRect(190, 90, 93, 28))
        self.checkBox_autostop = QCheckBox(self.groupBox_camera)
        self.checkBox_autostop.setObjectName(u"checkBox_autostop")
        self.checkBox_autostop.setGeometry(QRect(90, 20, 101, 20))
        self.checkBox_syncdisplay = QCheckBox(self.groupBox_camera)
        self.checkBox_syncdisplay.setObjectName(u"checkBox_syncdisplay")
        self.checkBox_syncdisplay.setGeometry(QRect(210, 20, 121, 20))

        self.gridLayout.addWidget(self.groupBox_camera, 1, 2, 1, 1)

        self.groupBox_screen = QGroupBox(self.centralwidget)
        self.groupBox_screen.setObjectName(u"groupBox_screen")
        self.groupBox_screen.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.groupBox_screen.sizePolicy().hasHeightForWidth())
        self.groupBox_screen.setSizePolicy(sizePolicy3)
        self.groupBox_screen.setMinimumSize(QSize(450, 50))
        self.pushButton_area = QPushButton(self.groupBox_screen)
        self.pushButton_area.setObjectName(u"pushButton_area")
        self.pushButton_area.setGeometry(QRect(90, 20, 75, 23))
        self.pushButton_full = QPushButton(self.groupBox_screen)
        self.pushButton_full.setObjectName(u"pushButton_full")
        self.pushButton_full.setGeometry(QRect(200, 20, 75, 23))

        self.gridLayout.addWidget(self.groupBox_screen, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1819, 21))
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuAbout.addAction(self.actionOpen_File)
        self.menuAbout.addAction(self.actionOpen_Folder)
        self.menuAbout.addAction(self.actionExport_template)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionEnter_License_Key)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dynamsoft Barcode Reader", None))
#if QT_CONFIG(accessibility)
        MainWindow.setAccessibleName(QCoreApplication.translate("MainWindow", u"Dynamsoft Barcode Reader", None))
#endif // QT_CONFIG(accessibility)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionOpen_File.setText(QCoreApplication.translate("MainWindow", u"Open File...", None))
        self.actionOpen_Folder.setText(QCoreApplication.translate("MainWindow", u"Open Folder...", None))
        self.actionExport_template.setText(QCoreApplication.translate("MainWindow", u"Save Template", None))
        self.actionEnter_License_Key.setText(QCoreApplication.translate("MainWindow", u"Enter License Key", None))
        self.groupBox_template.setTitle(QCoreApplication.translate("MainWindow", u"Template", None))
        self.pushButton_template.setText(QCoreApplication.translate("MainWindow", u"Load Template File", None))
        self.textEdit_template.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Paste template string here", None))
        self.pushButton_export_template.setText(QCoreApplication.translate("MainWindow", u"Export Template File", None))
        self.groupBox_barcode.setTitle(QCoreApplication.translate("MainWindow", u"Barcode Types", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"1D", None))
        self.checkBox_code39.setText(QCoreApplication.translate("MainWindow", u"Code 39", None))
        self.checkBox_code93.setText(QCoreApplication.translate("MainWindow", u"Code 93", None))
        self.checkBox_code128.setText(QCoreApplication.translate("MainWindow", u"Code 128", None))
        self.checkBox_codabar.setText(QCoreApplication.translate("MainWindow", u"Codabar", None))
        self.checkBox_itf.setText(QCoreApplication.translate("MainWindow", u"ITF", None))
        self.checkBox_ean13.setText(QCoreApplication.translate("MainWindow", u"EAN 13", None))
        self.checkBox_ean8.setText(QCoreApplication.translate("MainWindow", u"EAN 8", None))
        self.checkBox_upca.setText(QCoreApplication.translate("MainWindow", u"UPC A", None))
        self.checkBox_upce.setText(QCoreApplication.translate("MainWindow", u"UPC E", None))
        self.checkBox_industrial25.setText(QCoreApplication.translate("MainWindow", u"Industrial_25", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"2D", None))
        self.checkBox_qrcode.setText(QCoreApplication.translate("MainWindow", u"QR Code", None))
        self.checkBox_pdf417.setText(QCoreApplication.translate("MainWindow", u"PDF417", None))
        self.checkBox_aztec.setText(QCoreApplication.translate("MainWindow", u"Aztec", None))
        self.checkBox_postalcode.setText(QCoreApplication.translate("MainWindow", u"Postal Code", None))
        self.checkBox_maxicode.setText(QCoreApplication.translate("MainWindow", u"Maxi Code", None))
        self.checkBox_dotcode.setText(QCoreApplication.translate("MainWindow", u"DotCode", None))
        self.checkBox_patchcode.setText(QCoreApplication.translate("MainWindow", u"Patch Code", None))
        self.checkBox_datamatrix.setText(QCoreApplication.translate("MainWindow", u"DataMatrix", None))
        self.checkBox_gs1.setText(QCoreApplication.translate("MainWindow", u"GS1 Composite", None))
        self.label.setText("")
        self.textEdit_results.setDocumentTitle("")
        self.groupBox_camera.setTitle(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"640 x 480", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"320 x 240", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Resolution:", None))
        self.pushButton_open.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.checkBox_autostop.setText(QCoreApplication.translate("MainWindow", u"Auto Stop", None))
        self.checkBox_syncdisplay.setText(QCoreApplication.translate("MainWindow", u"Sync Display", None))
        self.groupBox_screen.setTitle(QCoreApplication.translate("MainWindow", u"Screen", None))
        self.pushButton_area.setText(QCoreApplication.translate("MainWindow", u"Select Area", None))
        self.pushButton_full.setText(QCoreApplication.translate("MainWindow", u"Fullscreen", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi
