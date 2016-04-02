from PyQt4 import QtGui  
import sys  
import fp 
import math 
import os  


class FpApp(QtGui.QMainWindow, fp.Ui_MainWindow): 
    def __init__(self):
        super(self.__class__, self).__init__()
        self.a = self.b = self.c = self.d = self.e = self.di = 0
        self.setupUi(self)  
        self.values()
        self.btn_value.clicked.connect(self.calculate)  
                                                            
    def values(self):
        if self.radioButton.isChecked() == False : 
            self.a = 3
            self.b = 4
            self.c = 3
            self.d = 7
            self.e = 5

        if self.radioButton_2.isChecked() == False : 
            self.a = 4
            self.b = 5
            self.c = 4
            self.d = 10
            self.e = 7
 
        if self.radioButton_3.isChecked() == False : 
            self.a = 6
            self.b = 7
            self.c = 6
            self.d = 15
            self.e = 10

    def calculate(self):
        inp = long(self.textEdit.toPlainText())
        out = long(self.textEdit_2.toPlainText())
        inq = long(self.textEdit_3.toPlainText())
        logfiles = long(self.textEdit_4.toPlainText())
        extfiles = long(self.textEdit_5.toPlainText())
        self.di = long(self.textEdit_6.toPlainText())
        UFP = self.a * inp + self.b * out + self.c * inq + self.d * logfiles + self.e * extfiles
        CAF = 0.65 + (0.01*self.di)
        FP = UFP + CAF
        self.label_6.setText(str(FP))
        self.label_6.setStyleSheet('color: green') 

def main():
    app = QtGui.QApplication(sys.argv)  
    form = FpApp()  
    form.show()  
    sys.exit(app.exec_())  


if __name__ == '__main__':  
    main()  