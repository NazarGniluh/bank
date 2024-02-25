from PyQt5.QtWidgets import *

def kalen():
    kalendari = QDialog()

    setWindowTitle('Календар')

    calendar = QCalendarWidget()
    calendar.setGridVisible(True)

    layout = QVBoxLayout()
    layout.addWidget(calendar)

    kalendari.show()
    kalendari.exec()