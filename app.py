
import pyqt
from pyqt import Window
from PyQt5.QtWidgets import QWidget, QApplication



app = Window(QWidget)

@app.view('home')
def home():
	pass

if __name__ == '__main__':
	app.show()