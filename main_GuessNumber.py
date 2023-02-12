import random 
import sys
from PySide6.QtWidgets import QApplication , QMainWindow ,  QMessageBox
from PySide6.QtUiTools import QUiLoader
from ui_guess import Ui_MainWindow
from functools import partial


class Guess_Number(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        self.guessbtn = self.ui.guessbtn
        self.textbtn = self.ui.textbtn
        self.resultbtn = self.ui.resultbtn
        self.user_num = 0
        self.counter = 0 
        self.computer_num = random.randint(1 , 30)
        self.guessbtn.clicked.connect(self.play)
        
    def play(self):

        self.user_num = int(self.textbtn.toPlainText())
        while self.computer_num != self.user_num  :
            self.counter +=  1
            if self.computer_num > self.user_num :
                self.resultbtn.setText(" GO UP🔺🔺\n"+"("+str(self.counter)+" guess)")
                break
            elif self.computer_num < self.user_num :
                self.resultbtn.setText(" GO DOWN🔻🔻\n"+"("+str(self.counter)+" guess)")    
                break
        else :
            if self.computer_num == self.user_num :
                message = QMessageBox()
                message.setText("🟢🔹🟣🔹🟢🔹🟣🔹🟢🔹🟣🔹🟢🔹\n🟣🔹🟢You Won After " + str(self.counter) + " Times🔹🟣🔹\n🟢🔹🟣🔹🟢🔹🟣🔹🟢🔹🟣🔹🟢🔹")
                message.exec()



app = QApplication(sys.argv)
main_window = Guess_Number()
main_window.show()



app.exec()