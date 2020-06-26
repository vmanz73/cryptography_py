# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kripto.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import vigenere as vig
import cesar as cs
import columnar as cl
import hashlib 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 536)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 591, 181))
        self.groupBox.setObjectName("groupBox")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(80, 70, 111, 17))
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 70, 17))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(80, 40, 111, 17))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 70, 17))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(440, 60, 70, 17))
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 110, 171, 17))
        self.label_6.setObjectName("label_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 210, 221, 241))
        self.groupBox_2.setObjectName("groupBox_2")
        self.rdVigenere = QtWidgets.QRadioButton(self.groupBox_2)
        self.rdVigenere.setGeometry(QtCore.QRect(20, 40, 114, 23))
        self.rdVigenere.setObjectName("rdVigenere")
        self.rdCaesar = QtWidgets.QRadioButton(self.groupBox_2)
        self.rdCaesar.setGeometry(QtCore.QRect(20, 90, 114, 23))
        self.rdCaesar.setObjectName("rdCaesar")
        self.rdColumn = QtWidgets.QRadioButton(self.groupBox_2)
        self.rdColumn.setGeometry(QtCore.QRect(20, 140, 191, 23))
        self.rdColumn.setObjectName("rdColumn")
        self.rdMD5 = QtWidgets.QRadioButton(self.groupBox_2)
        self.rdMD5.setGeometry(QtCore.QRect(20, 190, 114, 23))
        self.rdMD5.setObjectName("rdMD5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(290, 210, 331, 241))
        self.groupBox_3.setObjectName("groupBox_3")
        self.txtPlain = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtPlain.setGeometry(QtCore.QRect(90, 60, 221, 25))
        self.txtPlain.setObjectName("txtPlain")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 70, 17))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 180, 81, 17))
        self.label_9.setObjectName("label_9")
        self.txtChiper = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtChiper.setGeometry(QtCore.QRect(90, 180, 221, 25))
        self.txtChiper.setObjectName("txtChiper")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(20, 120, 70, 17))
        self.label_10.setObjectName("label_10")
        self.spinKey = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinKey.setEnabled(True)
        self.spinKey.setGeometry(QtCore.QRect(90, 120, 49, 26))
        self.spinKey.setObjectName("spinKey")
        self.txtKey = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtKey.setGeometry(QtCore.QRect(150, 120, 113, 25))
        self.txtKey.setObjectName("txtKey")
        self.btnProses = QtWidgets.QPushButton(self.centralwidget)
        self.btnProses.setGeometry(QtCore.QRect(480, 460, 91, 25))
        self.btnProses.setObjectName("btnProses")
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(370, 460, 91, 25))
        self.btnClear.setObjectName("btnClear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnProses.clicked.connect(self.proses)
        
    def proses(self):
        if self.txtChiper.text() == "":
            if self.rdVigenere.isChecked():
                key = vig.generateKey(self.txtPlain.text(),self.txtKey.text())
                chiper = vig.cipherText(self.txtPlain.text(),key)
                self.txtChiper.setText(chiper)
                print(key)
            if self.rdCaesar.isChecked():
                self.txtChiper.setText(cs.encrypt(int(self.spinKey.text()),self.txtPlain.text()))
            if self.rdColumn.isChecked():
                self.txtChiper.setText(cl.encryptMessage(self.txtPlain.text(),self.txtKey.text()))
            if self.rdMD5.isChecked():
                byt = bytes(self.txtPlain.text(), 'utf-8')
                md = hashlib.md5(byt).hexdigest()
                self.txtChiper.setText(md)

        elif self.txtPlain.text() == "":
            if self.rdVigenere.isChecked():
                key = vig.generateKey(self.txtChiper.text(),self.txtKey.text())
                plain = vig.originalText(self.txtChiper.text(),key)
                self.txtPlain.setText(plain)
                print(key)
            if self.rdCaesar.isChecked():
                self.txtPlain.setText(cs.decrypt(int(self.spinKey.text()),self.txtChiper.text()))
            if self.rdColumn.isChecked():
                self.txtPlain.setText(cl.decryptMessage(self.txtChiper.text(),self.txtKey.text()))
            

    def tes(self):
        self.txtKey.setText(self.spinKey.text())
        self.spinKey.setValue(0)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Identitas Mahasiswa"))
        self.label_4.setText(_translate("MainWindow", "18416255201024"))
        self.label.setText(_translate("MainWindow", "Nama :"))
        self.label_3.setText(_translate("MainWindow", "Tri Apriyanti"))
        self.label_2.setText(_translate("MainWindow", "Nim    :"))
        self.label_5.setText(_translate("MainWindow", "Foto"))
        self.label_6.setText(_translate("MainWindow", "Keamanan Komputer"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Kriptografi"))
        self.rdVigenere.setText(_translate("MainWindow", "Vigenere"))
        self.rdCaesar.setText(_translate("MainWindow", "Caesar"))
        self.rdColumn.setText(_translate("MainWindow", "Columnar Transposition"))
        self.rdMD5.setText(_translate("MainWindow", "MD5"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Hasil"))
        self.label_7.setText(_translate("MainWindow", "Plaintext"))
        self.label_9.setText(_translate("MainWindow", "Chipertext"))
        self.label_10.setText(_translate("MainWindow", "Key"))
        self.btnProses.setText(_translate("MainWindow", "Proses"))
        self.btnClear.setText(_translate("MainWindow", "Clear"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
