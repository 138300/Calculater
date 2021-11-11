from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from calculater import Ui_MainWindow

import math,pyperclip

class CalculaterWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.cal = Ui_MainWindow()
        self.cal.setupUi(self)  

        self.cal.n.setText('copy')  
        self.cal.n.clicked.connect(self.copy)

        self.cal.btn_clear.clicked.connect(self.clear)
        self.cal.btn_e.clicked.connect(self.result)

        # control operators button connection
        self.cal.btn_a.clicked.connect(self.addition)
        self.cal.btn_s.clicked.connect(self.subtract)
        self.cal.btn_d.clicked.connect(self.divide)
        self.cal.btn_m.clicked.connect(self.multiply)
        self.cal.btn_r.clicked.connect(self.radical)
        self.cal.btn_power.clicked.connect(self.power)
        
        # control digits buttons connection
        self.cal.btn_1.clicked.connect(self.btn_1)
        self.cal.btn_2.clicked.connect(self.btn_2)
        self.cal.btn_3.clicked.connect(self.btn_3)
        self.cal.btn_4.clicked.connect(self.btn_4)
        self.cal.btn_5.clicked.connect(self.btn_5)
        self.cal.btn_6.clicked.connect(self.btn_6)
        self.cal.btn_7.clicked.connect(self.btn_7)
        self.cal.btn_8.clicked.connect(self.btn_8)
        self.cal.btn_9.clicked.connect(self.btn_9)
        self.cal.btn_0.clicked.connect(self.btn_0)
        self.cal.btn_p.clicked.connect(self.btn_p)
        
        self.text=''

    def copy(self):
        pyperclip.copy(self.text)

    def clear(self):
        self.text = ''
        self.cal.label.setText('0')
   
    def result(self):
        if '÷' in self.text:
            self.text = self.text.replace('÷','/')
        if '×' in self.text:
            self.text = self.text.replace('×','*')
        try:
            self.text = eval(self.text)
            self.cal.label.setText(str(self.text))
            self.text = str(self.text)  
        except:
            if '/' in self.text:
                self.text = self.text.replace('/','÷')
            if '*' in self.text:
                self.text = self.text.replace('*','×')

    # region operators
    def addition(self):
        try:
         if self.text[-1] not in ['-','+','÷','×','.']:
                self.text += '+'
                self.cal.label.setText(self.text)

        except:
            pass
    def multiply(self):
        try:
           if self.text[-1] not in ['-','+','÷','×','.']:
                self.text += '×'
                self.cal.label.setText(self.text)
        except:
            pass
    def divide(self):
        try:
           if self.text[-1] not in ['-','+','÷','×','.']:
                self.text += '÷'
                self.cal.label.setText(self.text)
        except:
            pass
    def subtract(self):
        try:
            if self.text[-1] not in ['-','+','÷','×','.']:
                self.text += '-'
            self.cal.label.setText(self.text)  
        except:
            pass

    def power(self):
        try:
            self.text = math.pow(eval(self.cal.label.text()),2)
            self.cal.label.setText(str(self.text)) 
            self.text = str(eval(self.cal.label.text())**2)
        except:
            pass
    def radical(self):
        try:
            self.text = math.sqrt(eval(self.cal.label.text()))
            self.cal.label.setText(str(self.text))
            self.text=str(math.sqrt(eval(self.cal.label.text())))
        except:
            pass
    # endregion

    # region digits and point
    def btn_1(self):
        self.text += '1'
        self.cal.label.setText(self.text)

    def btn_2(self):
        self.text += '2'
        self.cal.label.setText(self.text)

    def btn_3(self):
        self.text += '3'
        self.cal.label.setText(self.text)

    def btn_4(self):
        self.text += '4'
        self.cal.label.setText(self.text)

    def btn_5(self):
        self.text += '5'
        self.cal.label.setText(self.text)

    def btn_6(self):
        self.text += '6'
        self.cal.label.setText(self.text)

    def btn_7(self):
        self.text += '7'
        self.cal.label.setText(self.text)

    def btn_8(self):
        self.text += '8'
        self.cal.label.setText(self.text)

    def btn_9(self):
        self.text += '9'
        self.cal.label.setText(self.text)

    def btn_0(self):
        self.text += '0'
        self.cal.label.setText(self.text)
    def btn_p(self):
        if self.text[-1] not in ['-','+','÷','×','.']:
            self.text += '.'
        self.cal.label.setText(self.text)
    # endregion
    
    


if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    window=CalculaterWindow()
    window.show()
    sys.exit(app.exec_())
