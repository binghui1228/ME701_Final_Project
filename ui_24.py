from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(665, 587)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 141, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Aharoni"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 30, 101, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Aharoni"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 60, 241, 361))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 191, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 201, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(114, 90, 101, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 201, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.listWidget = QtGui.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(10, 150, 221, 201))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(20, 30, 161, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(350, 60, 281, 371))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.pushButton_2 = QtGui.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 40, 261, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_5 = QtGui.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(20, 80, 171, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_3 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 120, 261, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton_3 = QtGui.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 160, 101, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 160, 111, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 221, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.listWidget_2 = QtGui.QListWidget(self.frame_2)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 220, 261, 141))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.label_10 = QtGui.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(20, 100, 161, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 480, 251, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 510, 431, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(300, 0, 20, 441))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Find Solution", None))
        self.label_2.setText(_translate("MainWindow", "Practice", None))
        self.label_3.setText(_translate("MainWindow", "Please input four integers:", None))
        self.pushButton.setText(_translate("MainWindow", "Show Solution", None))
        self.label_4.setText(_translate("MainWindow", "Here are some possible solutions:", None))
        self.label_9.setText(_translate("MainWindow", "(Format:2,3,4,5)", None))
        self.pushButton_2.setText(_translate("MainWindow", "Get Your Four Integers", None))
        self.label_5.setText(_translate("MainWindow", "Please input your solution:", None))
        self.pushButton_3.setText(_translate("MainWindow", "Show Solution", None))
        self.pushButton_4.setText(_translate("MainWindow", "Check my answer", None))
        self.label_6.setText(_translate("MainWindow", "Here are some possible solutions:", None))
        self.label_10.setText(_translate("MainWindow", "Use format:(1+2+3)*4", None))
        self.label_7.setText(_translate("MainWindow", "Choose four integers from 1 to 13.", None))
        self.label_8.setText(_translate("MainWindow", "Use addition,subtraction,multiplication and division to calculate 24.", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

