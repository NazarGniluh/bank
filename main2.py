from PyQt5.QtWidgets import *

import Kalendar
import Multiplayer
import main
import INterfeic
app = QApplication([])
app.setStyleSheet(
    """
    QPushButton:hover {
        background-color:yellow;
    }
    QWidget {
        background:rgb(255, 223, 0);
    }

    QPushButton
    {
        background-color: rgba(248, 252, 118, 0.8);

        font-size: 25px;a
        color: black;
        border-style: solid;
        border-width: 3px;
        border-color: khaki;
        border-radius: 10px;




    }

    """)

mainLine = QVBoxLayout()
LOn = QHBoxLayout()
Non = QHBoxLayout()
window = QWidget()
window.resize(100, 200)

Open_Kalendar = QPushButton("КАЛЕНДАР")

Open_Multiplayer = QPushButton("МЕДІЯПЛЕЄР")
text = QLabel("ДОБРИЙ ДЕНЬ, ВИ ВІЙШЛИ В ЛАУНЧЕР! НАЖМІТЬ КНОПКУ ЯКУ ПОДАНО НИЖЧЕ")

mainLine.addWidget(text)


LOn.addWidget(Open_Kalendar)
LOn.addWidget(Open_Multiplayer)

Open_Multiplayer.clicked.connect(Multiplayer.multi)
Open_Kalendar.clicked.connect(Kalendar.kalen)
mainLine.addLayout(LOn)



window.setLayout(mainLine)
window.show()
app.exec()