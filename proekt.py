from PyQt5.QtWidgets import *

app = QApplication([])
app.setStyleSheet("""
            QWidget {
                background: #003333;
            }
            
            
            QPushButton
            {
                background-color: #003333;
                border-style: outset;
                font-family: Roboto;
                
            }
            
        """)

window = QWidget()
window.resize(400, 400)

Open_Kalendar = QPushButton("КАЛЕНДАР")
Open_Multiplayer = QPushButton("МУЛЬТИПЛЕЄР")

olin = QVBoxLayout()
olin2 = QHBoxLayout()






window.setLayout(olin)
window.show()
app.exec()