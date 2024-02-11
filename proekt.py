from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(500, 500)

mainLine = QHBoxLayout()
Onsr = QVBoxLayout()






window.setLayout(mainLine)
window.show()
app.exec()