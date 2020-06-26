# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnPos = QtWidgets.QPushButton(self.centralwidget)
        self.btnPos.setGeometry(QtCore.QRect(250, 280, 91, 25))
        self.btnPos.setObjectName("btnPos")
        self.lblName = QtWidgets.QLabel(self.centralwidget)
        self.lblName.setGeometry(QtCore.QRect(260, 230, 70, 17))
        self.lblName.setObjectName("lblName")
        self.txtName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtName.setEnabled(True)
        self.txtName.setGeometry(QtCore.QRect(240, 200, 113, 25))
        self.txtName.setObjectName("txtName")
        self.rdEna = QtWidgets.QRadioButton(self.centralwidget)
        self.rdEna.setGeometry(QtCore.QRect(370, 110, 114, 23))
        self.rdEna.setObjectName("rdEna")
        self.rdDis = QtWidgets.QRadioButton(self.centralwidget)
        self.rdDis.setGeometry(QtCore.QRect(370, 150, 114, 23))
        self.rdDis.setObjectName("rdDis")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.rdEna.toggled.connect(self.radio)
        self.rdDis.toggled.connect(self.radio)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def radio(self):
        if self.rdDis.isChecked():
            self.txtName.setEnabled(False)
        if self.rdEna.isChecked():
            self.txtName.setEnabled(True)
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnPos.setText(_translate("MainWindow", "PushButton"))
        self.lblName.setText(_translate("MainWindow", "TextLabel"))
        self.rdEna.setText(_translate("MainWindow", "en"))
        self.rdDis.setText(_translate("MainWindow", "dis"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
