from PyQt5.QtWidgets import *
import main
import INterfeic
app = QApplication([])
app.setStyleSheet("""
            QWidget {
                background: #0085A6;
            }


            QPushButton
            {
                background-color: #004758;
                border-style: outset;
                font-family: Roboto;

            }

        """)

mainLine = QVBoxLayout()
LOn = QHBoxLayout()
Non = QHBoxLayout()
window = QWidget()
window.resize(200, 200)

Open_Kalendar = QPushButton("КАЛЕНДАР")
Open_Multiplayer = QPushButton("МУЛЬТИПЛЕЄР")
text = QLabel("ДОБРИЙ ДЕНЬ, ВИ ВІЙШЛИ В ЛАУНЧЕР!! НАЖМІТЬ НА КНОПКУ ЯКУ ПОДАНО ВНИЗУ")
mainLine.addWidget(text)

LOn.addWidget(Open_Kalendar)
LOn.addWidget(Open_Multiplayer)

mainLine.addLayout(LOn)



window.setLayout(mainLine)
window.show()
app.exec()