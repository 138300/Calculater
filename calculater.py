from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 730)
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../Users/M.ALI/Downloads/calculator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:#232931;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(470, 300))
        self.label.setWordWrap(True)
        self.label.scroll
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(66)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:#393E46;\n"
"color:white;\n"
"border-radius:50px;\n"
"padding:5px;"
"font-size:30px")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.row_1 = QtWidgets.QVBoxLayout()
        self.row_1.setObjectName("row_1")
        self.btn_power = QtWidgets.QPushButton(self.centralwidget)
        self.btn_power.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_power.setFont(font)
        self.btn_power.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_power.setStyleSheet("#btn_power{\n"
"    background-color:#4ECCA3;\n"
"border-radius:25px;\n"
"color:white;\n"
"\n"
"}\n"
"#btn_power::hover{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"}")
        self.btn_power.setObjectName("btn_power")
        self.row_1.addWidget(self.btn_power)
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1.setStyleSheet("#btn_1{\n"
"    background-color:#BBBFCA;\n"
"border-radius:25px;\n"
"color:white;\n"
"}\n"
"#btn_1::hover{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"}")
        self.btn_1.setObjectName("btn_1")
        self.row_1.addWidget(self.btn_1)
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_4.setStyleSheet("#btn_4{\n"
"    background-color:#BBBFCA;\n"
"border-radius:25px;\n"
"color:white;\n"
"}\n"
"#btn_4::hover{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"}")
        self.btn_4.setObjectName("btn_4")
        self.row_1.addWidget(self.btn_4)
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_7.setStyleSheet("#btn_7{\n"
"    background-color:#BBBFCA;\n"
"border-radius:25px;\n"
"color:white;\n"
"}\n"
"#btn_7::hover{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"}")
        self.btn_7.setObjectName("btn_7")
        self.row_1.addWidget(self.btn_7)
        self.btn_p = QtWidgets.QPushButton(self.centralwidget)
        self.btn_p.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_p.setFont(font)
        self.btn_p.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_p.setStyleSheet("#btn_p{\n"
"    background-color:#BBBFCA;\n"
"border-radius:25px;\n"
"color:white;\n"
"}\n"
"#btn_p::hover{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"}")
        self.btn_p.setObjectName("btn_p")
        self.row_1.addWidget(self.btn_p)
        self.horizontalLayout.addLayout(self.row_1)
        self.row_2 = QtWidgets.QVBoxLayout()
        self.row_2.setObjectName("row_2")
        self.btn_r = QtWidgets.QPushButton(self.centralwidget)
        self.btn_r.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_r.setFont(font)
        self.btn_r.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_r.setStyleSheet("#btn_r{\n"
"    background-color:#4ECCA3;\n"
"border-radius:25px;\n"
"color:white;\n"
"\n"
"}\n"
"#btn_r::hover{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"}")
        self.btn_r.setObjectName("btn_r")
        self.row_2.addWidget(self.btn_r)
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2.setStyleSheet("#btn_2{\n"
"    background-color:#BBBFCA;\n"
"border-radius:25px;\n"
"color:white;\n"
"\n"
"}\n"
"#btn_2::hover{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"}")
        self.btn_2.setObjectName("btn_2")
        self.row_2.addWidget(self.btn_2, 0, QtCore.Qt.AlignVCenter)
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_5.setStyleSheet("#btn_5{\n"
"    background-color:#BBBFCA;\n"
"border-radius:25px;\n"
"color:white;\n"
"\n"
"}\n"
"#btn_5::hover{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"}")
        self.btn_5.setObjectName("btn_5")
        self.row_2.addWidget(self.btn_5)
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_8.setStyleSheet("#btn_8{\n"
"    background-color:#BBBFCA;\n"
"border-radius:25px;\n"
"color:white;\n"
"\n"
"}\n"
"#btn_8::hover{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"}")
        self.btn_8.setObjectName("btn_8")
        self.row_2.addWidget(self.btn_8)
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_0.setFont(font)
        self.btn_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_0.setStyleSheet("#btn_0{\n"
"    background-color:#BBBFCA;\n"
"border-radius:25px;\n"
"color:white;\n"
"\n"
"}\n"
"#btn_0::hover{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"}")
        self.btn_0.setObjectName("btn_0")
        self.row_2.addWidget(self.btn_0)
        self.horizontalLayout.addLayout(self.row_2)
        self.row_3 = QtWidgets.QVBoxLayout()
        self.row_3.setObjectName("row_3")
        self.n = QtWidgets.QPushButton(self.centralwidget)
        self.n.setMinimumSize(QtCore.QSize(50, 70))
        self.n.setStyleSheet("#n{\n"
"    background-color:#4ECCA3;\n"
"font-size:24px;\n"
"border-radius:25px;\n"
"color:white;\n"
"\n"
"}\n"
"#n::hover{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"}")
        self.n.setText("")
        self.n.setObjectName("n")
        self.row_3.addWidget(self.n)
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_3.setStyleSheet("#btn_3{\n"
"    background-color:#BBBFCA;\n"
"border-radius:25px;\n"
"color:white;\n"
"\n"
"}\n"
"#btn_3::hover{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"}")
        self.btn_3.setObjectName("btn_3")
        self.row_3.addWidget(self.btn_3)
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_6.setStyleSheet("#btn_6{\n"
"    background-color:#BBBFCA;\n"
"border-radius:25px;\n"
"color:white;\n"
"\n"
"}\n"
"#btn_6::hover{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"}")
        self.btn_6.setObjectName("btn_6")
        self.row_3.addWidget(self.btn_6)
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_9.setStyleSheet("#btn_9{\n"
"    background-color:#BBBFCA;\n"
"border-radius:25px;\n"
"color:white;\n"
"\n"
"}\n"
"#btn_9::hover{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"}")
        self.btn_9.setObjectName("btn_9")
        self.row_3.addWidget(self.btn_9)
        self.btn_e = QtWidgets.QPushButton(self.centralwidget)
        self.btn_e.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_e.setFont(font)
        self.btn_e.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_e.setStyleSheet("#btn_e{\n"
"    background-color:#E84545;\n"
"border-radius:25px;\n"
"color:white;\n"
"\n"
"}\n"
"#btn_e::hover{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"}")
        self.btn_e.setObjectName("btn_e")
        self.row_3.addWidget(self.btn_e)
        self.horizontalLayout.addLayout(self.row_3)
        self.row_4 = QtWidgets.QVBoxLayout()
        self.row_4.setObjectName("row_4")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_clear.setFont(font)
        self.btn_clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_clear.setStyleSheet("#btn_clear{\n"
"    background-color:#E84545;\n"
"border-radius:25px;\n"
"color:white;\n"
"\n"
"}\n"
"#btn_clear::hover{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"}")
        self.btn_clear.setObjectName("btn_clear")
        self.row_4.addWidget(self.btn_clear)
        self.btn_d = QtWidgets.QPushButton(self.centralwidget)
        self.btn_d.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_d.setFont(font)
        self.btn_d.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_d.setStyleSheet("#btn_d{\n"
"    background-color:#4ECCA3;\n"
"border-radius:25px;\n"
"color:white;\n"
"\n"
"}\n"
"#btn_d::hover{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"}")
        self.btn_d.setObjectName("btn_d")
        self.row_4.addWidget(self.btn_d)
        self.btn_m = QtWidgets.QPushButton(self.centralwidget)
        self.btn_m.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_m.setFont(font)
        self.btn_m.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_m.setStyleSheet("#btn_m{\n"
"    background-color:#4ECCA3;\n"
"border-radius:25px;\n"
"color:white;\n"
"\n"
"}\n"
"#btn_m::hover{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"}")
        self.btn_m.setObjectName("btn_m")
        self.row_4.addWidget(self.btn_m)
        self.btn_a = QtWidgets.QPushButton(self.centralwidget)
        self.btn_a.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_a.setFont(font)
        self.btn_a.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_a.setStyleSheet("#btn_a{\n"
"    background-color:#4ECCA3;\n"
"border-radius:25px;\n"
"color:white;\n"
"\n"
"}\n"
"#btn_a::hover{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"}")
        self.btn_a.setObjectName("btn_a")
        self.row_4.addWidget(self.btn_a)
        self.btn_s = QtWidgets.QPushButton(self.centralwidget)
        self.btn_s.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_s.setFont(font)
        self.btn_s.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_s.setStyleSheet("#btn_s{\n"
"    background-color:#4ECCA3;\n"
"border-radius:25px;\n"
"color:white;\n"
"\n"
"}\n"
"#btn_s::hover{\n"
"background-color:#FF2E63;\n"
"color:white;\n"
"}")
        self.btn_s.setObjectName("btn_s")
        self.row_4.addWidget(self.btn_s)
        self.horizontalLayout.addLayout(self.row_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculater"))
        self.label.setText(_translate("MainWindow", "0"))
        self.btn_power.setText(_translate("MainWindow", "x²"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_p.setText(_translate("MainWindow", "."))
        self.btn_r.setText(_translate("MainWindow", "√"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_e.setText(_translate("MainWindow", "="))
        self.btn_clear.setText(_translate("MainWindow", "Clear"))
        self.btn_d.setText(_translate("MainWindow", "÷"))
        self.btn_m.setText(_translate("MainWindow", "×"))
        self.btn_a.setText(_translate("MainWindow", "+"))
        self.btn_s.setText(_translate("MainWindow", "-"))

