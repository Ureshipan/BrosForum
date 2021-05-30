import socket
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication
import resources_rc
import sys
import time


class Ui_BrosForum(object):
    def setupUi(self, BrosForum):
        BrosForum.setObjectName("BrosForum")
        BrosForum.setFixedSize(954, 560)
        self.centralwidget = QtWidgets.QWidget(BrosForum)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-4, 2, 961, 541))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 39, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 111, 21))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(730, 10, 221, 21))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(760, 39, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        #self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton.setGeometry(QtCore.QRect(790, 72, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        # self.pushButton.setFont(font)
        # self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 110, 891, 351))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 479, 791, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(830, 480, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 70, 201, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        BrosForum.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BrosForum)
        self.statusbar.setObjectName("statusbar")
        BrosForum.setStatusBar(self.statusbar)
        self.pushButton_2.clicked.connect(self.send)
        self.pushButton_3.clicked.connect(self.upd)
        self.scrollbar = self.textBrowser.verticalScrollBar()

        self.retranslateUi(BrosForum)
        QtCore.QMetaObject.connectSlotsByName(BrosForum)

    def retranslateUi(self, BrosForum):
        _translate = QtCore.QCoreApplication.translate
        BrosForum.setWindowTitle(_translate("BrosForum", "MainWindow"))
        self.label.setText(_translate("BrosForum", "<html><head/><body><p><img "
                                                   "src=\":/newPrefix/Background.jpg\"/></p></body></html>"))
        self.label_2.setText(_translate("BrosForum", "<html><head/><body><p><span style=\" font-size:14pt; "
                                                     "color:#ff0000;\">USERNAME</span></p></body></html>"))
        self.label_3.setText(_translate("BrosForum", "<html><head/><body><p align=\"center\"><span style=\" "
                                                     "font-size:14pt; font-weight:600; color:#ff0000;\">Connect to "
                                                     "private chat</span></p></body></html>"))
        self.lineEdit_2.setText(_translate("BrosForum", "Default_chat"))
        self.lineEdit.setText(_translate("BrosForum", username))
        #self.pushButton.setText(_translate("BrosForum", "CONNECT"))
        self.pushButton_2.setText(_translate("BrosForum", "SEND"))
        self.pushButton_3.setText(_translate("BrosForum", "UPDATE CHAT"))

    def send(self):
        global sock, username
        if self.lineEdit.text() != username:
            username = self.lineEdit.text()
            name_save = open('username.txt', 'w')
            name_save.write(username)
            name_save.close()
        year = time.strftime("%y")
        month = time.strftime("%m")
        day = time.strftime("%d")
        hour = time.strftime("%H")
        minute = time.strftime("%M")
        second = time.strftime("%S")
        cur_date = str(day) + '-' + str(month) + '-' + str(year) + '|' + ':'.join((hour, minute, second))
        mes = self.lineEdit_3.text()
        self.serv = self.lineEdit_2.text()
        self.lineEdit_3.setText('')
        if mes != '':
            sock.send(str(self.serv + '//' + '[' + cur_date + ']' + username + ':  ' + mes).encode())
        else:
            sock.send((self.serv + '//update').encode('utf-8'))
        self.upd()

    def upd(self):
        global all_chat, sock, start_coord, end_coord
        self.serv = self.lineEdit_2.text()
        sock.send((self.serv + '//update').encode('utf-8'))
        data = sock.recv(10240)
        all_chat = data.decode()
        all_chat = all_chat.split('\n')
        for i in range(len(all_chat)):
            if all_chat[i] == 'start':
                start_coord = i + 1
                break
        for j in range(start_coord, len(all_chat)):
            if all_chat[j] == 'end':
                end_coord = j
                break
        corr_chat = []
        for g in range(start_coord, end_coord):
            corr_chat.append(all_chat[g])
        corr_chat = '\n'.join(corr_chat)
        self.textBrowser.setText(corr_chat)
        self.scrollbar.setValue(self.scrollbar.maximum())


sock = socket.socket()
try:
    sock.connect(('37.110.95.116', 27735))
except:
    term = input('Подключение с сервером не установлено ')
    sys.exit()
username = ''
try:
    name_load = open(f'username.txt', 'r', encoding='utf-8')
    username = name_load.read()
    name_load.close()
except:
    namefile_create = open(f'username.txt', 'w', encoding='utf-8')
    namefile_create.write('Default_user')
    namefile_create.close
if username == '':
    username = 'Default_user'
all_chat = ''
start_coord = 0
end_coord = 0


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    BrosForum = QtWidgets.QMainWindow()
    ui = Ui_BrosForum()
    ui.setupUi(BrosForum)
    BrosForum.show()
    sys.exit(app.exec_())
