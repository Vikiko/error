import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import random
import numpy as np
import numpy.random
import time


a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
random.shuffle(a)
lis = a.tolist()
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('fci1.ui',self)
        self.randButton1.setText(str(lis[0]))  
        self.randButton2.setText(str(lis[1]))  
        self.randButton3.setText(str(lis[2]))  
        self.randButton4.setText(str(lis[3]))  
        self.randButton5.setText(str(lis[4]))  
        self.randButton6.setText(str(lis[5]))  
        self.randButton7.setText(str(lis[6]))  
        self.randButton8.setText(str(lis[7]))  
        self.randButton9.setText(str(lis[8]))  
        self.randButton10.setText(str(lis[9]))  
        self.randButton11.setText(str(lis[10]))  
        self.randButton12.setText(str(lis[11]))  
        self.randButton13.setText(str(lis[12]))  
        self.randButton14.setText(str(lis[13]))  
        self.randButton15.setText(str(lis[14]))  
        self.randButton16.setText(str(lis[15]))  
        self.randButton17.setText(str(lis[16]))  
        self.randButton18.setText(str(lis[17]))  
        self.randButton19.setText(str(lis[18]))  
        self.randButton20.setText(str(lis[19]))  
        self.randButton21.setText(str(lis[20]))  
        self.randButton22.setText(str(lis[21]))  
        self.randButton23.setText(str(lis[22]))  
        self.randButton24.setText(str(lis[23]))  
        self.randButton25.setText(str(lis[24]))
        self.rrrr4.setText('Старт')
        self.rrrr4.clicked.connect(self.hello)
    
    def hello(self):
        sec = 0
        while sec < 10:
            time.sleep(1)
            sec += 1  
            self.rrrr4.setText(str(sec))
    
        
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())